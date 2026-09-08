---
id: 06-pdes/complex-ginzburg-landau-blowup
title: "Blow-up for the Supercritical Complex Ginzburg-Landau Equation"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Blow-up for the Supercritical Complex Ginzburg-Landau Equation

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/complex-ginzburg-landau-blowup` · **Status:** open

## 1. Problem Statement / Conjecture

Consider the complex Ginzburg–Landau (CGL) equation for $u : \mathbb{R}^n \times [0,T) \to \mathbb{C}$,

$$\partial_t u = (1+i\beta)\,\Delta u + (1+i\delta)\,|u|^{p-1}u - \gamma u, \qquad u(\cdot,0)=u_0 \in H^1 \cap L^\infty,$$

with $p>1$ and real parameters $\beta,\delta,\gamma$. The equation interpolates between the nonlinear heat equation ($\beta=\delta=0$) and the focusing nonlinear Schrödinger equation (formal limit $\beta,\delta\to\infty$ after rescaling).

**Supercriticality** here has two independent meanings, and the open problem concerns both.

* **Parameter supercriticality.** All known blow-up constructions require the *subcritical* condition
  $$p - \delta^2 - \beta\delta(p+1) > 0 .$$
  Nothing is known when this quantity is negative — the *supercritical parameter regime*, where the dispersive rotation dominates the dissipative damping.
* **Exponent supercriticality.** $p > p_S := \frac{n+2}{n-2}$ ($n\ge 3$), where the nonlinearity is energy-supercritical for the Sobolev embedding, and in particular $p > p_{JL} := 1 + \frac{4}{n-4-2\sqrt{n-1}}$ for $n\ge 11$ (Joseph–Lundgren exponent), where type II blow-up is possible even for the real heat equation.

**Conjecture (blow-up in the supercritical regime).** For each $n\ge 1$ and each $p>1$ there exist $(\beta,\delta)$ with $p-\delta^2-\beta\delta(p+1)<0$ and initial data $u_0$ such that the corresponding solution blows up in finite time $T<\infty$, i.e. $\lim_{t\to T}\|u(t)\|_{L^\infty}=+\infty$. Moreover the blow-up is *not* of the standard self-similar type: no solution obeys $\|u(t)\|_{L^\infty}\sim C(T-t)^{-1/(p-1)}$ with the Masmoudi–Zaag profile.

A complete resolution requires either (a) construction of a blow-up solution with a rigorous description of its rate and profile in the supercritical parameter range, or (b) a global-existence theorem showing that all $H^1\cap L^\infty$ data yield global solutions there. The exponent-supercritical companion question — existence of **type II** blow-up ($\|u(t)\|_{L^\infty}(T-t)^{1/(p-1)}\to\infty$) for CGL with $p>p_S$ — is open even for $\beta=\delta=0$ in the range $p_S<p<p_{JL}$ and is fully open for $\delta \neq 0$.

## 2. Mathematical Foundations

**Function spaces and well-posedness.** For $\beta \in \mathbb{R}$ the semigroup $e^{t(1+i\beta)\Delta}$ is analytic on $L^q(\mathbb{R}^n)$, $1\le q<\infty$, with kernel $(4\pi(1+i\beta)t)^{-n/2}e^{-|x|^2/(4(1+i\beta)t)}$ and $\|e^{t(1+i\beta)\Delta}\|_{L^q\to L^q}\le C(1+\beta^2)^{n/4}$. Local well-posedness in $H^1\cap L^\infty$ follows by contraction (Ginibre–Velo, 1996–97), giving a maximal time $T$ with the blow-up alternative $T<\infty \Rightarrow \|u(t)\|_{L^\infty}\to\infty$.

**Scaling.** The equation with $\gamma=0$ is invariant under
$$u_\lambda(x,t) = \lambda^{\frac{2}{p-1}} u(\lambda x, \lambda^2 t),$$
critical for $\dot H^{s_c}$ with $s_c = \frac n2 - \frac{2}{p-1}$. Energy-criticality is $s_c=1$, i.e. $p=p_S$.

**Similarity variables.** Fix $a\in\mathbb{R}^n$ and set
$$y=\frac{x-a}{\sqrt{T-t}},\quad s=-\log(T-t),\quad w(y,s)=(T-t)^{\frac{1+i\delta}{p-1}}u(x,t).$$
Then $w$ solves
$$\partial_s w = (1+i\beta)\Delta w - \tfrac12\, y\cdot\nabla w - \frac{1+i\delta}{p-1}\,w + (1+i\delta)|w|^{p-1}w - e^{-s}\gamma w .$$
Constant solutions are $w \equiv \kappa e^{i\theta}$ with $\kappa = (p-1)^{-1/(p-1)}$; the phase invariance $w\mapsto e^{i\theta}w$ makes the set of equilibria a circle, so the linearized operator always carries a zero mode from phase rotation.

**Linearized operator.** Writing $w=\kappa+\varepsilon$ and splitting into real and imaginary parts, the linearization is
$$\mathcal{L}_{\beta}\varepsilon = (1+i\beta)\Delta \varepsilon - \tfrac12 y\cdot\nabla\varepsilon + \text{(matrix potential)},$$
whose real part is the Hermite operator $\mathcal{L}=\Delta - \frac12 y\cdot\nabla$ with spectrum $\{-m/2 : m\in\mathbb{N}\}$ in $L^2(e^{-|y|^2/4}dy)$ and Hermite-polynomial eigenfunctions. The real component has eigenvalues $1-\frac m2$ (two unstable modes $m=0,1$, one neutral $m=2$); the imaginary component has eigenvalues $-\frac m2$ and hence a neutral mode at $m=0$ (phase) and $m=2$.

**Blow-up profile (subcritical parameters).** Masmoudi–Zaag (2008) construct solutions with
$$u(x,t) \sim \big[(p-1)(T-t)\big]^{-\frac{1+i\delta}{p-1}}\left(p-1+\frac{b\,|x-a|^2}{(T-t)|\log(T-t)|}\right)^{-\frac{1+i\delta}{p-1}},\qquad b=\frac{(p-1)^2}{4\big(p-\delta^2-\beta\delta(p+1)\big)} .$$
The construction requires $b>0$, i.e. exactly the subcriticality condition of §1. The critical case $p-\delta^2-\beta\delta(p+1)=0$ has a *different* profile with rate $|\log(T-t)|^{-1/2}$ corrections (Nouaili–Zaag).

**No gradient structure.** For $\delta\ne 0$ the equation admits no Lyapunov functional; the real heat-equation energy $E(w)=\int(\frac12|\nabla w|^2 - \frac{1}{p+1}|w|^{p+1})\rho$ is not monotone, and no maximum principle applies to complex-valued $u$.

## 3. History & State of the Art (SOTA)

CGL arose as the universal amplitude equation near a Hopf bifurcation in dissipative systems (Newell–Whitehead, Stewartson–Stuart, 1969–71); the physics literature is surveyed by Aranson–Kramer (*Rev. Mod. Phys.* 2002). Blow-up in the "backward-bifurcation" (focusing) case with $\gamma>0$ was observed numerically in the 1990s.

Milestones:

* **1996–97.** Ginibre–Velo: Cauchy theory in local and Lebesgue spaces, global existence for $|\delta|$ large relative to $p$ (dissipation-dominated regime).
* **1998.** Zaag: blow-up profile for vector-valued heat equations with no gradient structure — the technical template later used for CGL.
* **2001.** Plecháč–Šverák: computer-assisted / matched-asymptotic study of radial self-similar singular solutions of CGL in $n=3,4$, showing a discrete family of profiles and a parameter threshold beyond which the self-similar branch disappears.
* **2008.** Masmoudi–Zaag: rigorous construction and stability of blow-up solutions with the $(p-1+b|z|^2)^{-(1+i\delta)/(p-1)}$ profile under $p-\delta^2-\beta\delta(p+1)>0$ and $|\beta|,|\delta|$ small.
* **2013–14.** Cazenave–Dickstein–Weissler: finite-time blow-up for $\partial_t u = e^{i\theta}(\Delta u + |u|^{\alpha}u)$ for $|\theta|$ below an explicit threshold, via a modified (rotated) energy and a concavity/Levine argument; Cazenave–Dias–Figueira extend to linear driving $-\gamma u$.
* **2018–2022.** Nouaili–Zaag (ARMA 2018) handle the **critical** case $p-\delta^2-\beta\delta(p+1)=0$; Duong–Nouaili–Zaag extend to a range of critical parameters with a $\log$-corrected profile.

State of the art: blow-up is proven only for parameters at or below the criticality threshold, and only for the standard type I rate.

## 4. Partial Results / Verified Cases

* **Subcritical parameters, all $n\ge 1$, all $p>1$:** if $|\beta|,|\delta|$ are small and $p-\delta^2-\beta\delta(p+1)>0$, there is an open (stable, codimension-0 modulo translation/phase) set of $H^1\cap L^\infty$ data blowing up at a single point with the explicit profile of §2 and rate $\|u(t)\|_\infty\sim \kappa\,(T-t)^{-1/(p-1)}$ (Masmoudi–Zaag 2008).
* **Critical parameters $p=\delta^2+\beta\delta(p+1)$:** blow-up solutions exist with modified profile in which the quadratic term is replaced by a $|y|^2/s$ term at a different scale (Nouaili–Zaag 2018; Duong–Nouaili–Zaag).
* **$\beta=\delta=0$ (real heat equation):** complete type I theory — Giga–Kohn, Merle–Zaag (Duke 1997) for stability, Velázquez for the size of the blow-up set. Type II blow-up exists for $p>p_{JL}$, $n\ge 11$ (Herrero–Velázquez 1994) and is *excluded* for $p_S<p<p_{JL}$ in the radial class (Matano–Merle 2004).
* **Rotated equation $e^{i\theta}(\Delta u+|u|^\alpha u)$:** finite-time blow-up for $|\theta|<\theta_0(\alpha,n)$ with $\theta_0>0$ explicit; here $\theta$ small corresponds to $\beta=\delta=\tan\theta$ (Cazenave–Dickstein–Weissler 2013).
* **Global existence:** for $|\delta|$ sufficiently large relative to $p$ (specifically when the nonlinearity is "dissipative", $\mathrm{Re}\big[(1+i\delta)|u|^{p-1}u\,\bar u\big]$ controlled), all $H^1$ solutions are global (Ginibre–Velo).
* **One dimension, $n=1$, cubic $p=3$:** numerics (Popp–Stiller–Kuznetsov–Kramer, *Physica D* 1998) show blow-up for a broad parameter window including some supercritical $(\beta,\delta)$ — *unproven*.

## 5. Principal Obstacles

* **No maximum principle, no energy.** For $\delta\ne0$ the solution is genuinely complex-valued, so comparison arguments, intersection-number (zero-number) techniques, and the Giga–Kohn Lyapunov functional in similarity variables all fail. Type I *a priori* bounds — the cornerstone of the real theory — are unavailable.
* **Degeneration of the profile.** The constant $b=\frac{(p-1)^2}{4(p-\delta^2-\beta\delta(p+1))}$ changes sign at the threshold. For $b<0$ the candidate profile $(p-1+b|z|^2)^{-(1+i\delta)/(p-1)}$ becomes singular at finite $|z|$, so the ansatz that drives every existing construction has no admissible continuation. It is not a matter of a harder fixed-point argument: the object one is trying to construct does not exist in that class.
* **Spectral degeneracy.** In the supercritical range the $m=2$ (neutral) mode of the linearized operator changes stability character; the finite-dimensional topological (Brouwer degree / shooting) argument used to control the unstable directions requires the neutral modes to be genuinely slaved by the $1/s$ correction, which fails when $b<0$.
* **Loss of smallness.** All constructions treat $(\beta,\delta)$ perturbatively around the real heat equation. Supercriticality in the parameter sense typically requires $|\delta|>\sqrt p$, i.e. $O(1)$ or large parameters — outside every perturbative regime.
* **Energy-supercritical exponents.** For $p>p_S$ there is no coercive conserved or monotone quantity; even for NLS, blow-up in the defocusing energy-supercritical case was only reached by the Merle–Raphaël–Rodnianski–Szeftel (2022) compressible-Euler front, a technique with no known parabolic-dispersive analogue.

## 6. The Gap

Proven: blow-up with an explicit type I profile whenever $p-\delta^2-\beta\delta(p+1)\ge 0$ and $|\beta|,|\delta|$ small.

Conjectured: blow-up (of some type) when $p-\delta^2-\beta\delta(p+1)<0$.

The precise missing step is a **substitute for the degenerate self-similar ansatz**. One must either (i) exhibit a new family of self-similar profiles $w(y,s)=\varphi(y)$ solving
$$(1+i\beta)\Delta\varphi - \tfrac12 y\cdot\nabla\varphi - \frac{1+i\delta}{p-1}\varphi + (1+i\delta)|\varphi|^{p-1}\varphi = 0$$
that are bounded on $\mathbb{R}^n$ and nonconstant in the supercritical range — the ODE shooting problem studied numerically by Plecháč–Šverák, whose solution branch appears to terminate at a threshold — or (ii) prove a genuinely non-self-similar (type II) blow-up, requiring a new inner/outer matching with an unknown modulation law, or (iii) prove global existence, which would need a coercive quantity that nobody has found for $\delta\ne 0$.

## 7. Current Research (as of June 2026)

* **Zaag's group (Paris 13 / Paris-Dauphine — Nouaili, Duong, Zaag).** Extending the constructive spectral method beyond the critical case; the working programme is to push the parameter range past $p=\delta^2+\beta\delta(p+1)$ by adding logarithmic corrections at successive orders. Partial results in the "slightly supercritical" window $0 < \delta^2+\beta\delta(p+1)-p \ll 1$ are announced *(frontier — verify)*.
* **Computer-assisted proofs.** Rigorous interval-arithmetic continuation of the Plecháč–Šverák self-similar branch (in the style of van den Berg–Lessard radii-polynomial methods) is an active direction; a validated existence proof for one supercritical profile would settle the conjecture in that instance *(frontier — verify)*.
* **Dispersive-side techniques.** Adaptation of the Merle–Raphaël–Rodnianski–Szeftel front-compression mechanism to weakly dissipative complex equations; the dissipation term is a singular perturbation of the compressible-Euler ansatz and its effect on the front is not understood *(frontier — verify)*.
* **Neural / high-precision numerics.** Adaptive-mesh and physics-informed-network computations of CGL singularities in $n=2,3$ report rate-corrections consistent with type II behaviour in the supercritical window *(frontier — verify)*.

## 8. Future Work

1. **Classify bounded self-similar profiles** of the elliptic system above as $(\beta,\delta)$ vary — a two-parameter bifurcation analysis of a nonautonomous complex ODE. Identify the exact threshold at which the branch disappears and whether it disappears by blow-up of the shooting parameter or by collision with a second branch.
2. **Construct type II solutions** by matching an inner rescaled steady state (a Ginzburg–Landau vortex-type or ground-state solution) to a self-similar outer region, with modulation rate $\lambda(t)$ determined by a solvability condition — the parabolic analogue of the Herrero–Velázquez mechanism, adapted to a non-self-adjoint linearization.
3. **Seek a monotone quantity for $\delta\ne 0$**, e.g. a rotated energy $E_\theta$ monotone along the flow for $\theta$ in a range strictly larger than the Cazenave–Dickstein–Weissler threshold; this would give blow-up by convexity for a larger parameter set.
4. **Settle the exponent-supercritical case $\beta=\delta=0$, $p_S<p<p_{JL}$, non-radial**, where Matano–Merle's exclusion of type II uses zero-number arguments valid only for radial real solutions.
5. **Numerical–rigorous bridge:** validated numerics for a single supercritical parameter pair, then continuation.

## 9. Key References

- **[Foundational]** J. Ginibre, G. Velo. *The Cauchy problem in local spaces for the complex Ginzburg–Landau equation, I. Compactness methods.* Physica D **95** (1996), 191–228; *II. Contraction methods.* Comm. Math. Phys. **187** (1997), 45–79.
- **[Foundational]** H. Zaag. *Blow-up results for vector-valued nonlinear heat equations with no gradient structure.* Ann. Inst. H. Poincaré Anal. Non Linéaire **15** (1998), 581–622.
- **[Foundational]** F. Merle, H. Zaag. *Stability of the blow-up profile for equations of the type $u_t=\Delta u+|u|^{p-1}u$.* Duke Math. J. **86** (1997), 143–195.
- **[SOTA]** N. Masmoudi, H. Zaag. *Blow-up profile for the complex Ginzburg–Landau equation.* J. Funct. Anal. **255** (2008), 1613–1666.
- **[SOTA]** N. Nouaili, H. Zaag. *Construction of a blow-up solution for the complex Ginzburg–Landau equation in a critical case.* Arch. Ration. Mech. Anal. **228** (2018), 995–1058.
- **[SOTA]** G. K. Duong, N. Nouaili, H. Zaag. *Construction of blowup solutions for the complex Ginzburg–Landau equation with critical parameters.* Memoirs of the American Mathematical Society (2022).
- **[SOTA]** T. Cazenave, F. Dickstein, F. B. Weissler. *Finite-time blowup for a complex Ginzburg–Landau equation.* SIAM J. Math. Anal. **45** (2013), 244–266.
- **[SOTA]** T. Cazenave, J. P. Dias, M. Figueira. *Finite-time blowup for a complex Ginzburg–Landau equation with linear driving.* J. Evol. Equ. **14** (2014), 403–415.
- **[Structural]** P. Plecháč, V. Šverák. *On self-similar singular solutions of the complex Ginzburg–Landau equation.* Comm. Pure Appl. Math. **54** (2001), 1215–1242.
- **[Comparison]** M. A. Herrero, J. J. L. Velázquez. *Explosion de solutions d'équations paraboliques semilinéaires supercritiques.* C. R. Acad. Sci. Paris Sér. I **319** (1994), 141–145.
- **[Comparison]** H. Matano, F. Merle. *On nonexistence of type II blowup for a supercritical nonlinear heat equation.* Comm. Pure Appl. Math. **57** (2004), 1494–1541.
- **[Comparison]** F. Merle, P. Raphaël, I. Rodnianski, J. Szeftel. *On blow up for the energy super critical defocusing nonlinear Schrödinger equations.* Invent. Math. **227** (2022), 247–413.
- **[Survey]** I. S. Aranson, L. Kramer. *The world of the complex Ginzburg–Landau equation.* Rev. Mod. Phys. **74** (2002), 99–143.
- **[Survey/Book]** P. Quittner, P. Souplet. *Superlinear Parabolic Problems: Blow-up, Global Existence and Steady States.* 2nd ed., Birkhäuser, 2019.

## 10. Worked Example / Concrete Special Case

**Space-independent solution and the origin of the phase logarithm.** Take $\gamma=0$ and $u_0$ constant, so $\Delta u\equiv 0$ and
$$u' = (1+i\delta)|u|^{p-1}u .$$
Write $u=\rho e^{i\phi}$ with $\rho>0$. Separating modulus and phase:
$$\rho' = \rho^{p}, \qquad \phi' = \delta\,\rho^{p-1}.$$
The first gives $\rho(t) = \big[(p-1)(T-t)\big]^{-\frac{1}{p-1}}$ with $T = \rho_0^{-(p-1)}/(p-1)$. Substituting into the second:
$$\phi'(t) = \frac{\delta}{(p-1)(T-t)} \;\Longrightarrow\; \phi(t) = \phi_0 - \frac{\delta}{p-1}\log(T-t).$$
So
$$u(t) = \big[(p-1)(T-t)\big]^{-\frac{1+i\delta}{p-1}} e^{i\phi_0}.$$
The modulus blows up at rate $(T-t)^{-1/(p-1)}$ while the phase winds infinitely often — this is why the similarity change of variables in §2 uses the *complex* exponent $\frac{1+i\delta}{p-1}$.

**Where supercriticality bites.** Perturb around this ODE solution with a quadratic profile in the self-similar variable $z = y/\sqrt{s}$, $y=x/\sqrt{T-t}$, $s=-\log(T-t)$:
$$w(y,s) \approx \varphi(z) = \left(p-1+b|z|^2\right)^{-\frac{1+i\delta}{p-1}} .$$
Insert into the similarity equation and collect the $O(1/s)$ terms. The quadratic coefficient must satisfy the solvability relation
$$4b\,\frac{p-\delta^2-\beta\delta(p+1)}{(p-1)^2} = 1, \qquad\text{i.e.}\qquad b = \frac{(p-1)^2}{4\big(p-\delta^2-\beta\delta(p+1)\big)} .$$

Numbers. Take $p=3$, $\beta=0$.
* $\delta = 1$: $p-\delta^2 = 2>0$, so $b = 4/8 = 1/2 >0$. The profile $\varphi(z)=(2+\tfrac12|z|^2)^{-(1+i)/2}$ is bounded, decays, and the Masmoudi–Zaag theorem applies: a stable one-point blow-up solution exists.
* $\delta = \sqrt3$: $p-\delta^2 = 0$. Critical case; $b=+\infty$. The quadratic ansatz breaks and one must rescale $z$ by a further power of $s$ — this is the Nouaili–Zaag regime.
* $\delta = 2$: $p-\delta^2 = -1 < 0$, so $b = -1$. The candidate profile is $(2-|z|^2)^{-(1+i)/2}$, which is singular at $|z|=\sqrt2$ — a *spurious* second singularity at a fixed self-similar radius. No admissible profile exists in this family.

The last line is the whole difficulty in miniature: at $\delta=2$, $p=3$, $\beta=0$ the equation
$$\partial_t u = \Delta u + (1+2i)|u|^{2}u$$
is expected on numerical grounds to blow up, but the only rigorously constructed profile degenerates, and no replacement — self-similar or type II — is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*