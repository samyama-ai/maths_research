---
id: 06-pdes/constantin-lax-majda-blow-up
title: "Constantin-Lax-Majda Equation Blow-Up"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Constantin-Lax-Majda Equation Blow-Up

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/constantin-lax-majda-blow-up` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Constantin–Lax–Majda (CLM) equation is the one-dimensional vorticity model

$$\partial_t \omega = \omega\, H\omega, \qquad \omega(\cdot,0)=\omega_0,$$

where $H$ is the Hilbert transform. It retains the vortex-stretching term of the 3D Euler vorticity equation and deletes advection. Constantin, Lax and Majda solved it in closed form in 1985: generic smooth data blow up in finite time. That part is **closed**.

The open problem is the *advective* family that interpolates between CLM and 3D Euler — the generalized CLM (gCLM) equation of Okamoto–Sakajo–Wunsch,

$$\partial_t\omega + a\,u\,\partial_x\omega = \omega\,\partial_x u, \qquad \partial_x u = H\omega, \qquad a\in\mathbb{R},$$

with $a=0$ the CLM equation and $a=1$ the De Gregorio equation. The governing questions:

1. **(De Gregorio on $S^1$, smooth data.)** Is every solution with $\omega_0\in C^\infty(S^1)$ global? Conjectured **yes** (global regularity, with convergence to a steady state).
2. **(De Gregorio on $\mathbb{R}$, smooth data.)** Does there exist $\omega_0\in C_c^\infty(\mathbb{R})$ whose solution blows up in finite time? Blow-up is known for $C^\alpha$ data with small $\alpha$; the $C^\infty$ case is open.
3. **(Threshold in $a$.)** Determine the critical value(s) $a_c$ separating finite-time singularity from global existence, for each regularity class and domain.

A complete resolution means: for a fixed domain ($S^1$ or $\mathbb{R}$), a fixed regularity class, and each $a$, either a proof of global well-posedness or an explicit construction of data with $\limsup_{t\to T^-}\|\omega(t)\|_{L^\infty}=\infty$ for some $T<\infty$.

## 2. Mathematical Foundations

**Hilbert transform.** On $\mathbb{R}$,
$$H f(x) = \frac{1}{\pi}\,\mathrm{p.v.}\!\int_{\mathbb{R}} \frac{f(y)}{x-y}\,dy,$$
and on $S^1=\mathbb{R}/2\pi\mathbb{Z}$,
$$H f(x) = \frac{1}{2\pi}\,\mathrm{p.v.}\!\int_{-\pi}^{\pi} f(x-y)\cot\!\left(\frac{y}{2}\right) dy .$$
$H$ is bounded on $L^p$, $1<p<\infty$, satisfies $H^2=-\mathrm{Id}$ (mod constants), and $\widehat{Hf}(k)=-i\,\mathrm{sgn}(k)\hat f(k)$.

**Model origin.** The 3D Euler vorticity equation is $\partial_t\omega + (u\cdot\nabla)\omega = (\nabla u)\,\omega$ with $\nabla u = \mathcal{S}[\omega]$ a matrix of Calderón–Zygmund singular integrals of $\omega$. CLM replace $\mathcal{S}$ by $H$ — the canonical 1D CZ operator of the same $0$-order homogeneity — and drop the transport term. The Beale–Kato–Majda criterion transfers: the solution persists as long as $\int_0^T\|\omega(t)\|_{L^\infty}dt<\infty$.

**Key algebraic identity.** If $f+iHf$ and $g+iHg$ are boundary values of Hardy-space functions, their product is too, giving
$$H(fg - Hf\,Hg) = f\,Hg + g\,Hf .$$

**Complexification.** Set $u_x = H\omega$ and $z = H\omega + i\omega$. Using the identity above with $f=g$-type pairings,
$$\partial_t z = \tfrac12 z^2,$$
a pointwise complex Riccati ODE. Hence
$$z(x,t) = \frac{z_0(x)}{1-\tfrac{t}{2}z_0(x)}, \qquad
\boxed{\ \omega(x,t)=\frac{4\,\omega_0(x)}{\bigl(2-t\,H\omega_0(x)\bigr)^2 + t^2\omega_0(x)^2}\ }$$

**Blow-up criterion (Constantin–Lax–Majda 1985).** The solution is global iff the denominator never vanishes, i.e. iff $H\omega_0(x)\le 0$ at every zero $x$ of $\omega_0$. Otherwise
$$T_* = \frac{2}{\max\{H\omega_0(x)\;:\;\omega_0(x)=0\}},$$
and $\|\omega(t)\|_{L^\infty}\sim C(T_*-t)^{-1}$.

**gCLM steady states.** For $a=1$ on $S^1$, $\omega = A\sin(x+x_0)$ is an exact steady state for every $A,x_0$: $u_x=H\omega=-A\cos(x+x_0)$, $u=-A\sin(x+x_0)$, and $u\omega_x = u_x\omega$ identically. This family is the "ground state" around which the global-regularity conjecture is organized.

## 3. History & State of the Art (SOTA)

- **1985.** Constantin, Lax and Majda introduce the model in *Comm. Pure Appl. Math.* and give the explicit formula above. The lesson: vortex stretching alone, with a $0$-order nonlocal operator, produces singularities; advection must be the regularizing mechanism in Euler.
- **1986.** Schochet shows that adding viscosity, $\partial_t\omega=\omega H\omega+\nu\omega_{xx}$, does not restore global existence for all data — the viscous model still blows up.
- **1990.** De Gregorio restores advection, $a=1$, arguing that transport can deplete the nonlinearity; numerics suggested global existence on $S^1$.
- **2005.** Córdoba–Córdoba–Fontelos prove finite-time blow-up for $\partial_t\theta + (H\theta)\theta_x = 0$ (the $a=-1$ scaling, with dissipation $\Lambda^\gamma$, $\gamma<1/2$) — the first blow-up theorem for a transport-with-nonlocal-velocity model without an explicit formula.
- **2008.** Okamoto, Sakajo and Wunsch define the one-parameter family and map it numerically: blow-up for $a$ below a threshold, apparent global existence above.
- **2019–2021.** The modern wave. Jia–Stewart–Šverák prove nonlinear stability of the $A\sin x$ ground state for De Gregorio on $S^1$; Lei–Liu–Ren prove global existence on $S^1$ for sign-definite data; Elgindi–Jeong and Chen–Hou–Huang prove finite-time blow-up for $|a|$ small and for $a=1$ on $\mathbb{R}$ in Hölder classes.
- **2021.** Elgindi's $C^{1,\alpha}$ blow-up for 3D Euler uses a fundamental model whose structure and stability analysis descend directly from the CLM/De Gregorio lineage; Chen–Hou's computer-assisted 3D Euler singularity with boundary uses the same self-similar-plus-stability architecture.

## 4. Partial Results / Verified Cases

| Case | Result |
|---|---|
| $a=0$ (CLM), $\mathbb{R}$ or $S^1$, any $\omega_0\in H^1$ | **Fully solved.** Explicit formula; blow-up iff $H\omega_0>0$ at some zero of $\omega_0$; rate $(T_*-t)^{-1}$. |
| $a=0$ with viscosity $\nu>0$ | Blow-up persists for suitable data (Schochet 1986); explicit solutions available. |
| $a=-1$ with dissipation $\Lambda^\gamma$, $0\le\gamma<1/2$ | Finite-time blow-up (Córdoba–Córdoba–Fontelos 2005). |
| $a<0$, $\mathbb{R}$ | Blow-up for a class of positive/odd data (Castro–Córdoba 2008; Elgindi–Jeong 2020). |
| $|a|$ small, $C^\alpha$ data | Finite-time self-similar blow-up (Elgindi–Jeong 2020, ARMA 235). |
| $a=1$ (De Gregorio) on $\mathbb{R}$, $C_c^\alpha$ data, $\alpha>0$ small | Finite-time blow-up, asymptotically self-similar (Chen–Hou–Huang, CPAM 2021). |
| $a=1$ on $S^1$, $\omega_0$ of one sign | Global existence; solution converges to a steady state (Lei–Liu–Ren, CMP 2020). |
| $a=1$ on $S^1$, $\omega_0$ near $A\sin x$ in a weighted norm | Global existence and nonlinear stability of the ground state (Jia–Stewart–Šverák 2019; Chen, ARMA 2021, for $a$ near $1$). |
| gCLM with strong dissipation $\Lambda^\gamma$, $\gamma\ge 1$ | Global regularity in standard function classes. |

## 5. Principal Obstacles

- **The $\alpha\to 0$ degeneration.** All known blow-up proofs for $a\ne 0$ work in $C^\alpha$ with $\alpha$ *small*, because the approximate self-similar profile is built by perturbing off the $\alpha=0$ CLM solution. As $\alpha\to 1$ the advection term $a\,u\omega_x$ ceases to be a perturbation of the stretching term: $u$ gains a full derivative of regularity from $\omega$ only in the scaling-critical sense, so the linearized operator's spectral gap closes. No method currently produces a self-similar profile at $\alpha=1$ or in $C^\infty$.
- **Advection is neither uniformly good nor uniformly bad.** Transport rotates the phase of $z$ and moves the would-be singular point away from the stretching maximum. Energy methods see only $\frac{d}{dt}\|\omega\|_{L^p}^p = (1+\tfrac{a}{p}\cdot p)\!\int\!\omega^p H\omega$-type identities in which the advective contribution integrates to a *sign-indefinite* commutator; there is no coercive functional known that captures the competition.
- **Loss of the exact structure.** The Riccati linearization $\partial_t z=\frac12 z^2$ is destroyed by any $a\ne 0$: $u\omega_x$ is not the imaginary part of an analytic-in-$z$ expression. Complex-analytic and Möbius-invariance methods (Lushnikov–Silantyev–Siegel) survive only for special $a$ and special pole configurations.
- **Marginal Fourier analysis.** $H$ is order $0$; $\omega\mapsto \omega H\omega$ loses no derivatives but is not $L^\infty$-bounded on $\mathrm{BMO}$-scale spaces. Paraproduct decompositions give local well-posedness in $H^s$, $s>3/2$, and nothing about the lifespan.
- **Stability of the profile.** Even where a self-similar profile is constructed numerically, converting it into a theorem requires proving a spectral gap for a non-self-adjoint linearized operator with continuous spectrum touching the imaginary axis. Chen–Hou–Huang overcome this with weighted energy estimates plus computer assistance; the weights are hand-tuned to $\alpha$ and do not extend.

## 6. The Gap

Proven: blow-up for $a=1$ in $C^\alpha_c(\mathbb{R})$ for *some* small $\alpha>0$; global existence on $S^1$ for one-signed or ground-state-nearby data. Conjectured: global regularity for all smooth data on $S^1$, and (open, undecided) the fate of general smooth data on $\mathbb{R}$.

The exact barrier is the **regularity threshold in the self-similar construction**. One needs either

- a self-similar or asymptotically self-similar solution of $\Omega + (\lambda y + a\,U)\Omega_y = \Omega U_y$ (the profile equation after $\omega\sim(T-t)^{-1}\Omega(y/(T-t)^{\mu})$) with $\Omega\in C^\infty$ and adequate decay — currently only $C^\alpha$ profiles are known to exist; or
- a global Lyapunov functional on $S^1$ dominating the stretching term for *all* smooth data, extending the sign-definite and near-ground-state arguments to sign-changing, far-from-$\sin x$ data.

Closing either half would also decide whether the $a$-threshold $a_c$ is regularity-dependent — the numerics of Okamoto–Sakajo–Wunsch suggest it is.

## 7. Current Research (as of June 2026)

- **Caltech (Hou and collaborators).** Rigorous computer-assisted schemes: interval-arithmetic verification of approximate self-similar profiles plus energy-based stability, transferred from gCLM to Boussinesq and 3D Euler with boundary. Current effort targets raising $\alpha$ toward $1$ in the De Gregorio profile. *(frontier — verify)*
- **Duke / NYU (Elgindi, Jeong, Drivas).** Structural approach: identify which nonlocal-velocity models admit "fundamental model" reductions with exact scaling symmetry, and classify the $a$-dependence of the leading-order profile.
- **Minnesota (Šverák school).** Dynamical-systems viewpoint on $S^1$: the $A\sin x$ family as an attractor, gradient-flow-like structure, and the conjecture that all smooth solutions converge to a rotated ground state.
- **Madrid (Córdoba, Castro, Gómez-Serrano).** Nonlocal transport equations, $\Lambda^\gamma$-dissipative thresholds, and rigorous numerics for singular profiles.
- **Machine-learned profiles.** Physics-informed neural networks used to generate high-accuracy approximate self-similar solutions of gCLM as the starting point of computer-assisted proofs. *(frontier — verify)*

## 8. Future Work

1. **Push $\alpha\to 1$.** Construct a $C^{1}$ or $C^{1,\alpha}$ self-similar profile for De Gregorio on $\mathbb{R}$; the obstruction is the vanishing spectral gap, so a new weighted norm adapted to the far field is needed.
2. **Prove the $S^1$ global-regularity conjecture** by finding a monotone quantity — candidates include $\int (\omega_x/\omega)^2$-type quantities on nodal intervals used in the sign-definite case.
3. **Locate $a_c$ rigorously.** Combine the $|a|$-small blow-up results with an $a$-large global-existence proof to sandwich the threshold.
4. **Transfer to Euler.** Determine which parts of the De Gregorio argument survive when $H$ is replaced by a genuinely 2D/3D Riesz-transform structure, in particular for axisymmetric Euler without swirl.
5. **Dissipative critical exponent.** Settle blow-up versus global existence for gCLM with $\Lambda^\gamma$, $\gamma\in[1/2,1)$, the analogue of the critical SQG problem.

## 9. Key References

- **[Foundational]** P. Constantin, P. D. Lax, A. Majda. *A simple one-dimensional model for the three-dimensional vorticity equation.* Communications on Pure and Applied Mathematics, 38(6):715–724, 1985.
- **[Foundational]** S. De Gregorio. *On a one-dimensional model for the three-dimensional vorticity equation.* Journal of Statistical Physics, 59:1251–1263, 1990.
- **[Foundational]** S. Schochet. *Explicit solutions of the viscous model vorticity equation.* Communications on Pure and Applied Mathematics, 39(4):531–537, 1986.
- **[Foundational]** A. Córdoba, D. Córdoba, M. A. Fontelos. *Formation of singularities for a transport equation with nonlocal velocity.* Annals of Mathematics, 162(3):1377–1389, 2005.
- **[SOTA / Recent]** H. Okamoto, T. Sakajo, M. Wunsch. *On a generalization of the Constantin–Lax–Majda equation.* Nonlinearity, 21(10):2447–2461, 2008.
- **[SOTA / Recent]** A. Castro, D. Córdoba. *Global existence, singularities and ill-posedness for a nonlocal flux.* Advances in Mathematics, 219(6):1916–1936, 2008.
- **[SOTA / Recent]** H. Jia, S. Stewart, V. Šverák. *On the De Gregorio modification of the Constantin–Lax–Majda model.* Archive for Rational Mechanics and Analysis, 231:1269–1304, 2019.
- **[SOTA / Recent]** T. M. Elgindi, I.-J. Jeong. *On the effects of advection and vortex stretching.* Archive for Rational Mechanics and Analysis, 235:1763–1817, 2020.
- **[SOTA / Recent]** Z. Lei, J. Liu, X. Ren. *On the Constantin–Lax–Majda model with convection.* Communications in Mathematical Physics, 375:765–783, 2020.
- **[SOTA / Recent]** J. Chen, T. Y. Hou, D. Huang. *On the finite time blowup of the De Gregorio model for the 3D Euler equations.* Communications on Pure and Applied Mathematics, 74(6):1282–1350, 2021.
- **[SOTA / Recent]** J. Chen. *On the slightly perturbed De Gregorio model on $S^1$.* Archive for Rational Mechanics and Analysis, 241:1843–1869, 2021.
- **[SOTA / Recent]** P. M. Lushnikov, D. A. Silantyev, M. Siegel. *Collapse versus blow-up and global existence in the generalized Constantin–Lax–Majda equation.* Journal of Nonlinear Science, 31:82, 2021.
- **[SOTA / Recent]** T. M. Elgindi. *Finite-time singularity formation for $C^{1,\alpha}$ solutions to the incompressible Euler equations on $\mathbb{R}^3$.* Annals of Mathematics, 194(3):647–727, 2021.
- **[Survey]** A. J. Majda, A. L. Bertozzi. *Vorticity and Incompressible Flow.* Cambridge University Press, 2002 (Chapter 5 treats the CLM model).
- **[Survey]** T. D. Drivas, T. M. Elgindi. *Singularity formation in the incompressible Euler equation in finite and infinite time.* EMS Surveys in Mathematical Sciences, 10(1):1–100, 2023.

## 10. Worked Example / Concrete Special Case

Take the CLM equation ($a=0$) on $S^1$ with $\omega_0(x)=\sin x$. On the circle, $H(\sin x) = -\cos x$, so $H\omega_0(x) = -\cos x$.

**Blow-up criterion.** The zeros of $\omega_0$ are $x=0$ and $x=\pi$. There $H\omega_0(0)=-1$ and $H\omega_0(\pi)=+1$. Since $H\omega_0>0$ at $x=\pi$, the solution blows up, at time
$$T_* = \frac{2}{\max\{H\omega_0(x):\omega_0(x)=0\}} = \frac{2}{1} = 2 .$$

**Explicit solution.** Substituting into the CLM formula,
$$\omega(x,t)=\frac{4\sin x}{(2+t\cos x)^2 + t^2\sin^2 x}
=\frac{4\sin x}{\,t^2 + 4t\cos x + 4\,}.$$
The denominator $D(x,t)=t^2+4t\cos x+4 = (t+2\cos x)^2+4\sin^2 x$ vanishes only when $\sin x=0$ and $t=-2\cos x$, i.e. at $(x,t)=(\pi,2)$. For $t<2$, $D\ge (t-2)^2>0$ and $\omega$ is smooth.

**Local structure.** Put $x=\pi+y$. Then $\cos x = -1+\tfrac{y^2}{2}+O(y^4)$, $\sin x = -y+O(y^3)$, and
$$D = t^2-4t+4+2ty^2+O(y^4) = (t-2)^2 + 2t\,y^2 + O(y^4).$$
Writing $s=2-t\to 0^+$ and using $2t\to 4$,
$$\omega(\pi+y,t)\;\approx\; \frac{-4y}{s^2+4y^2} \;=\; \frac{1}{s}\,\Phi\!\left(\frac{y}{s}\right),\qquad \Phi(\xi)=\frac{-4\xi}{1+4\xi^2}.$$
So the blow-up is exactly self-similar with scaling exponents $(1,1)$: amplitude $\sim s^{-1}$, width $\sim s$.

**Norm behaviour.** $\max_\xi|\Phi|=1$ at $\xi=\pm\tfrac12$, so
$$\|\omega(t)\|_{L^\infty}\sim \frac{1}{2-t}\to\infty, \qquad \int_0^{T_*}\|\omega\|_{L^\infty}dt=\infty,$$
consistent with the BKM criterion. Meanwhile $\|\omega(t)\|_{L^1}$ stays bounded (the profile has $\Phi\in L^1$-borderline logarithmic divergence cut off by the circle), and $\|\omega(t)\|_{L^p}\sim s^{-1+1/p}$ for $p>1$: the singularity is $L^1$-subcritical and $L^p$-supercritical for every $p>1$.

**Contrast with $a=1$.** Adding the advection term $u\omega_x$ with $u=-\sin x$ turns this very datum into an *exact steady state* — $\omega(x,t)=\sin x$ for all $t$. The single term that is dropped in CLM converts a $(T_*-t)^{-1}$ singularity into an eternal equilibrium. That is the whole difficulty of the open problem in one line.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*