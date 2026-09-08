---
id: 06-pdes/damped-driven-nls-attractor
title: "Global Attractors for the Damped Driven Nonlinear Schrodinger Equation"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Attractors for the Damped Driven Nonlinear Schrödinger Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/damped-driven-nls-attractor` · **Status:** open

## 1. Problem Statement / Conjecture

Consider the weakly damped, forced nonlinear Schrödinger equation (DDNLS)

$$ i\,\partial_t u + \Delta u + i\gamma u + \lambda |u|^{2\sigma} u = f, \qquad u(0)=u_0, $$

with $\gamma>0$, $\lambda=\pm 1$ (focusing $+$, defocusing $-$), $\sigma>0$, time-independent forcing $f$, on a domain $\Omega\subseteq\mathbb{R}^d$ ($\Omega$ bounded with Dirichlet conditions, the torus $\mathbb{T}^d$, or $\Omega=\mathbb{R}^d$).

**The problem.** Determine, for which $(d,\sigma,\lambda,\Omega)$ and in which phase space $X$ ($L^2$, $H^1$, $H^s$), the solution semigroup $S(t)$ possesses a compact global attractor
$$ \mathcal{A}=\bigcap_{\tau\ge 0}\overline{\bigcup_{t\ge\tau} S(t)\mathcal{B}}^{\,X}, $$
and describe it: finite fractal dimension $d_f(\mathcal{A})<\infty$, regularity/analyticity, sharp dependence of $d_f$ on $\gamma$, $\|f\|$ and $|\Omega|$, and existence of exponential attractors and finitely many determining modes.

**Conjecture (attractor conjecture for DDNLS).** For every $d\ge1$, every energy-subcritical or energy-critical $\sigma$ ($\sigma<\tfrac{2}{d-2}$, resp. $\sigma=\tfrac{2}{d-2}$ for $d\ge3$), defocusing $\lambda=-1$, and $f\in L^2$, the DDNLS semigroup on $H^1$ is well defined and has a compact global attractor of finite fractal dimension, with $\mathcal{A}\subset H^{1+s}$ for $f\in H^s$. A complete solution requires either a proof at this generality or a counterexample — a parameter regime where the ball-absorbing dynamics fails to be asymptotically compact, or where $d_f(\mathcal{A})=\infty$.

**Sharp-dimension sub-problem.** Close the gap between upper bounds $d_f(\mathcal{A})\le C(\gamma,\|f\|,|\Omega|)$ obtained from Lyapunov-exponent / volume-contraction arguments and the (much smaller) lower bounds obtained from instability of explicit equilibria.

## 2. Mathematical Foundations

**Conservation structure.** For $\gamma=f=0$ the flow conserves mass and energy
$$ M(u)=\int_\Omega |u|^2, \qquad E(u)=\int_\Omega \Big(|\nabla u|^2-\tfrac{\lambda}{\sigma+1}|u|^{2\sigma+2}\Big). $$
With damping and forcing, multiplying by $\bar u$ and taking imaginary parts gives the mass balance
$$ \tfrac{d}{dt}\|u\|_{L^2}^2 + 2\gamma\|u\|_{L^2}^2 = 2\,\mathrm{Im}\!\int f\bar u \;\le\; \gamma\|u\|^2_{L^2}+\gamma^{-1}\|f\|^2_{L^2}, $$
hence $\limsup_{t\to\infty}\|u(t)\|_{L^2}^2\le \gamma^{-2}\|f\|_{L^2}^2$: an absorbing ball in $L^2$ exists unconditionally. Pairing with $\partial_t\bar u$ gives the energy balance
$$ \tfrac{d}{dt}E(u) + 2\gamma\!\int\!|\nabla u|^2 - \tfrac{2\gamma\lambda}{\sigma+1}\!\int\!|u|^{2\sigma+2} = \text{(forcing terms)}, $$
which is *not* sign-definite unless the nonlinear term is controlled — the defocusing case $\lambda=-1$ gives a good sign, the focusing case does not.

**Semigroup and attractor.** $S(t):X\to X$, $S(t)u_0=u(t)$, is a continuous semigroup once global well-posedness holds. A compact global attractor exists iff $S(t)$ has a bounded absorbing set $\mathcal{B}$ and is asymptotically compact on $\mathcal{B}$ (Temam, 1997). Since the Schrödinger group is unitary and has **no smoothing**, asymptotic compactness cannot be obtained by parabolic regularization; it must be produced by dispersion, by an energy-equation (Ball) argument, or by a splitting into a decaying rough part and a compact smooth part.

**Fractal dimension bound.** Linearizing about a trajectory $u(t)\subset\mathcal{A}$,
$$ i\partial_t v + \Delta v + i\gamma v + \lambda\big(( \sigma{+}1)|u|^{2\sigma}v + \sigma|u|^{2\sigma-2}u^2\bar v\big)=0, $$
and estimating the trace $\mathrm{Tr}\,(L(u)\circ Q_m)$ of the linearization on $m$-dimensional volumes yields $d_f(\mathcal{A})\le m_\ast$ where $m_\ast$ is the first $m$ making the $m$-trace negative (Constantin–Foias–Temam machinery). The damping supplies $-\gamma m$; the nonlinear term supplies a positive contribution controlled by $\|u\|_{L^\infty}^{2\sigma}$, giving bounds polynomial in $\gamma^{-1}\|f\|_{L^2}$ and in $|\Omega|$.

**Critical exponents.** $\sigma=2/d$ is mass-critical; $\sigma=2/(d-2)$ ($d\ge3$) is energy-critical. Scaling $u_\mu(t,x)=\mu^{1/\sigma}u(\mu^2 t,\mu x)$ leaves the equation invariant only for $\gamma=f=0$; damping and forcing break scaling, so criticality enters only through the local theory.

## 3. History & State of the Art

- **1986–88.** Numerical studies of the damped driven focusing cubic NLS on a periodic box (Bishop, Forest, McLaughlin, Overman) reveal quasi-periodic routes to chaos and low-dimensional attractors; this motivated the rigorous theory.
- **1988.** Ghidaglia proves the first rigorous result: for $d=1$ (and $d=2$ subcritical) on bounded domains, DDNLS has a compact global attractor in $H^1_0$ of finite Hausdorff and fractal dimension, with explicit bounds in $\gamma$, $\|f\|$ and the domain size.
- **1995.** X. Wang gives a clean *energy-equation* proof of asymptotic compactness (following Ball's method), removing compactness-of-embedding requirements and extending to $\mathbb{R}^d$ in low dimensions. Laurençot treats $\mathbb{R}^N$, $N\le3$, subcritical.
- **1996–98.** Goubet establishes attractor **regularity**: the $H^1$ attractor of the 1D cubic DDNLS lies in $H^2$ (and in $H^{1+s}$ for $f\in H^s$), by splitting the Duhamel solution into a linearly damped low-regularity part and a smoother nonlinear part. He extends this to $\mathbb{R}^2$.
- **1998.** Oliver–Titi prove **Gevrey/analyticity** of the attractor for the 1D DDNLS with analytic forcing, and bound the number of determining nodes.
- **2009.** Goubet–Molinet construct the global attractor in the low-regularity space $L^2(\mathbb{R})$ for the subcritical 1D equation, using Bourgain $X^{s,b}$ spaces and profile decomposition.
- **2010s–2020s.** Extensions to fractional/half-wave damped equations, weakly damped NLS with white-noise or quasi-periodic forcing (Kuksin–Shirikyan style), nonlocal damping, and attempts at the energy-critical case using concentration-compactness (Kenig–Merle) plus damping. Zelik's 2023 survey situates DDNLS among the "non-smoothing" attractor problems, where the theory is still incomplete.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $d=1$, $\Omega$ bounded, cubic $\sigma=1$, both signs of $\lambda$ | Compact attractor in $H^1_0$, $d_f(\mathcal{A})<\infty$ | Ghidaglia (1988) |
| $d=1,2$ subcritical, $\Omega=\mathbb{R}^d$ | Attractor in $H^1$ via energy equation / asymptotic compactness | Wang (1995), Laurençot (1995) |
| $d=1$, $\Omega=\mathbb{R}$, $\sigma<2$ | Attractor in $L^2(\mathbb{R})$ | Goubet–Molinet (2009) |
| $d=1$ cubic, $f\in H^s$ | $\mathcal{A}\subset H^{1+s}$; analytic if $f$ analytic | Goubet (1996), Oliver–Titi (1998) |
| $d=2$, $\Omega=\mathbb{R}^2$, cubic | Attractor is bounded in $H^2$ | Goubet (1998) |
| $d=3$, defocusing cubic ($\sigma=1$, subcritical), bounded $\Omega$ | Attractor exists in $H^1_0$ under global well-posedness in $H^1$ | Laurençot (1995) and successors |
| All above | $d_f(\mathcal{A})\le$ polynomial in $\gamma^{-1}\|f\|_{L^2}$, $|\Omega|$ | Ghidaglia (1988) |

Unresolved in all dimensions: **energy-critical** $\sigma=2/(d-2)$, $d\ge3$; **whole-space $d\ge3$**; focusing mass-supercritical regimes where solutions may blow up before damping acts; existence of **exponential attractors** with explicit dimension in $\mathbb{R}^d$.

## 5. Principal Obstacles

- **No parabolic smoothing.** The linear group $e^{it\Delta}$ is unitary on every $H^s$; damping multiplies it by $e^{-\gamma t}$ but does not gain a derivative. Compactness of the absorbing set — automatic for reaction–diffusion or damped-wave systems via $H^2\hookrightarrow\hookrightarrow H^1$ plus smoothing — has to be manufactured by hand.
- **Loss of compactness at infinity.** On $\mathbb{R}^d$, bounded sets in $H^1$ are not precompact in $L^2$; solutions can carry mass to spatial infinity. Ball's energy method fixes this only when a *global* energy identity with the right signs is available, i.e. essentially in the defocusing subcritical case.
- **Critical nonlinearity.** At $\sigma=2/(d-2)$ the Strichartz-based local theory has no room: the time of local existence depends on the profile of the data, not merely its $H^1$ norm. Uniform-in-time bounds on the absorbing ball then do not translate into uniform Duhamel splittings, so Goubet's regularity scheme breaks.
- **Focusing case.** For $\lambda=+1$ and $\sigma\ge 2/d$, damping does not prevent finite-time blow-up for large data; $S(t)$ may not be globally defined, and only a local/conditional attractor theory is possible.
- **Dimension estimates are lossy.** Volume-contraction bounds use $\|u\|_{L^\infty(\mathcal A)}$ through crude Sobolev/Agmon inequalities, producing exponents far above what modulational-instability lower bounds suggest.

## 6. The Gap

Proven: existence, regularity and finite dimension for $d\le2$ (and $d=3$ subcritical on bounded domains), defocusing or small-data focusing, with polynomial dimension bounds. Conjectured: the same in the energy-critical case and on unbounded domains in $d\ge3$.

The precise missing step is an **asymptotic-compactness mechanism robust at criticality**: a decomposition
$$ u(t)=v(t)+w(t), \qquad \|v(t)\|_{H^1}\le Ce^{-\gamma t/2},\quad \|w(t)\|_{H^{1+\varepsilon}}\le R, $$
uniformly over the absorbing ball, when the local well-posedness time is not bounded below by a function of $\|u\|_{H^1}$ alone. Concentration-compactness gives a minimal non-compact profile; what is missing is a **damped Morawetz/interaction-Morawetz estimate** ruling that profile out uniformly in $t$. Separately, for the dimension: no construction produces an unstable manifold of dimension matching the $\gamma^{-\alpha}\|f\|^{\beta}$ upper bound, so even the correct power of $\gamma$ is unknown.

## 7. Current Research (as of June 2026)

- **Critical damped dispersive attractors.** Groups following Zelik (Surrey / Lanzhou) and Kostianko adapt the "smooth attractor for quintic damped wave" toolbox (Strichartz + backward uniqueness + energy-to-Strichartz bootstrap) to NLS. *(frontier — verify)*
- **Low-regularity attractors.** Goubet's Amiens school and collaborators extend the $L^2(\mathbb{R})$ construction to fractional Schrödinger, half-wave and derivative NLS with damping, using $X^{s,b}$ and profile decompositions.
- **Randomly forced NLS.** Replacing $f$ by white-in-time noise turns the question into ergodicity of a unique stationary measure (Kuksin–Shirikyan programme); recent work asks whether the support of that measure is the deterministic attractor's stochastic analogue. *(frontier — verify)*
- **Exponential attractors and determining modes**, sharpening Oliver–Titi node counts, and rigorous-numerics reconstruction of low-dimensional chaotic attractors for the 1D focusing damped-driven cubic NLS.

## 8. Future Work

1. Prove a **damped interaction Morawetz inequality** giving uniform-in-time $L^4_{t,x}$ bounds on the absorbing ball for defocusing energy-critical DDNLS in $\mathbb{R}^3$; this would close the $d\ge3$ whole-space case.
2. Construct **lower bounds** on $d_f(\mathcal{A})$ by counting unstable modes of explicit equilibria (Section 10) as $\gamma\to0$, and compare with Ghidaglia's upper bound to identify the sharp exponent.
3. Establish **exponential attractors** (finite-dimensional, exponentially attracting, robust) for $d=2$ — currently open because standard squeezing needs smoothing.
4. Determine whether $\mathcal{A}$ is **$C^\infty$ for $C^\infty$ forcing** in $d\ge2$, extending Goubet's $H^2$ result.
5. Characterize the **focusing case with damping**: is there a threshold $\|f\|_\ast(\gamma)$ below which all solutions are global and an attractor exists?

## 9. Key References

- **[Foundational]** J.-M. Ghidaglia. *Finite-dimensional behavior for weakly damped driven Schrödinger equations.* Annales de l'IHP, Analyse Non Linéaire, 5(4):365–405, 1988.
- **[Foundational]** R. Temam. *Infinite-Dimensional Dynamical Systems in Mechanics and Physics*, 2nd ed. Applied Mathematical Sciences 68, Springer, 1997.
- **[Method]** X. Wang. *An energy equation for the weakly damped driven nonlinear Schrödinger equations and its application to their attractors.* Physica D, 88(3–4):167–175, 1995.
- **[Regularity]** O. Goubet. *Regularity of the attractor for a weakly damped nonlinear Schrödinger equation.* Applicable Analysis, 60(1–2):99–119, 1996.
- **[Regularity]** O. Goubet. *Regularity of the attractor for a weakly damped nonlinear Schrödinger equation in $\mathbb{R}^2$.* Advances in Differential Equations, 3(3):337–360, 1998.
- **[Analyticity]** M. Oliver, E. S. Titi. *Analyticity of the attractor and the number of determining nodes for a weakly damped driven nonlinear Schrödinger equation.* Indiana University Mathematics Journal, 47(1):49–73, 1998.
- **[SOTA]** O. Goubet, L. Molinet. *Global attractor for weakly damped nonlinear Schrödinger equations in $L^2(\mathbb{R})$.* Nonlinear Analysis: TMA, 71(1–2):317–320, 2009.
- **[Unbounded domains]** P. Laurençot. *Long-time behaviour for weakly damped driven nonlinear Schrödinger equations in $\mathbb{R}^N$, $N\le 3$.* NoDEA, 2(3):357–369, 1995.
- **[Well-posedness]** T. Cazenave. *Semilinear Schrödinger Equations.* Courant Lecture Notes 10, AMS, 2003.
- **[Well-posedness]** J. Bourgain. *Global Solutions of Nonlinear Schrödinger Equations.* AMS Colloquium Publications 46, 1999.
- **[Dynamics/numerics]** A. R. Bishop, M. G. Forest, D. W. McLaughlin, E. A. Overman II. *A quasi-periodic route to chaos in a near-integrable PDE.* Physica D, 23(1–3):293–328, 1986.
- **[Survey]** S. Zelik. *Attractors. Then and now.* Russian Mathematical Surveys, 78(4):635–777, 2023.
- **[Stochastic forcing]** S. Kuksin, A. Shirikyan. *Mathematics of Two-Dimensional Turbulence.* Cambridge University Press, 2012.

## 10. Worked Example / Concrete Special Case

**Setting.** $\Omega=\mathbb{T}_L=[0,L]$ with periodic conditions, cubic focusing $\lambda=+1$, $\sigma=1$, constant forcing $f\in\mathbb{C}$:
$$ i u_t + u_{xx} + i\gamma u + |u|^2u = f. $$

**Step 1 — the spatially uniform equilibrium.** Seek $u(t,x)\equiv a\in\mathbb{C}$. Then $i\gamma a + |a|^2 a = f$, i.e. $a(s+i\gamma)=f$ with $s:=|a|^2$. Taking moduli:
$$ s\,(s^2+\gamma^2)=|f|^2 \quad\Longleftrightarrow\quad s^3+\gamma^2 s=|f|^2 . $$
The left side is strictly increasing in $s>0$, so there is **exactly one** positive root $s=s(\gamma,|f|)$, hence a unique constant equilibrium $a=f/(s+i\gamma)$ — a point of $\mathcal{A}$ for every $\gamma,f$.

**Step 2 — linearize.** Rotate phase, $u=e^{i\arg a}(|a|+w)$, and drop quadratic terms:
$$ i w_t + w_{xx} + i\gamma w + s(2w+\bar w)=0 . $$
Insert the mode $w = p\,e^{ikx} + \bar q\, e^{-ikx}$, $k=2\pi n/L$, $n\in\mathbb{Z}$. With $A:=k^2-2s$ one gets
$$ \dot p = -i\big(Ap - s q\big)-\gamma p, \qquad \dot q = \;\;i\big(Aq - s p\big)-\gamma q . $$
The $2\times2$ matrix has zero trace and determinant $A^2-s^2$, so its eigenvalues are $\mu_\pm=-\gamma\pm\sqrt{s^2-A^2}$.

**Step 3 — instability window.** The mode $k$ is unstable iff
$$ |k^2-2s|<s \quad\text{and}\quad \sqrt{s^2-(k^2-2s)^2}>\gamma, $$
i.e. $k^2\in(s,3s)$ with a strict growth condition; the growth is maximal at $k^2=2s$, where $\mu_+=s-\gamma$. So the constant state is unstable as soon as
$$ s>\gamma \quad\Longleftrightarrow\quad |f|^2 = s^3+\gamma^2 s > 2\gamma^3 \quad\Longleftrightarrow\quad |f|>\sqrt{2}\,\gamma^{3/2}, $$
**provided** some admissible wavenumber $2\pi n/L$ lies in the band. For $L$ large the band $(\sqrt{s},\sqrt{3s})$ contains
$$ N(L)\;\approx\;\frac{L}{2\pi}\big(\sqrt{3s}-\sqrt{s}\big)\cdot 2 \;=\;\frac{L\sqrt{s}}{\pi}\big(\sqrt{3}-1\big) $$
integers $n$ (counting $\pm n$), each contributing a two-real-dimensional unstable direction. Hence
$$ d_f(\mathcal{A}) \;\ge\; \dim W^u(a) \;\gtrsim\; L\sqrt{s}\;\sim\; L\,|f|^{2/3}\quad (\gamma\ll |f|^{2/3}). $$

**Step 4 — reading off the open problem.** This lower bound grows like $L|f|^{2/3}$, while the trace-formula upper bound of Ghidaglia is a strictly larger power of $\gamma^{-1}\|f\|$ and of $L$. Numerically (Bishop–Forest–McLaughlin–Overman) the observed attractor for this exact system is low-dimensional and chaotic, with dimension of the order of the number of unstable sidebands — suggesting the lower bound is closer to the truth. Proving that matching upper bound, and doing the analogous construction in $d\ge2$ at critical $\sigma$, is precisely what remains open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*