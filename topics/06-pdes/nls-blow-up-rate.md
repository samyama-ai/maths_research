---
id: 06-pdes/nls-blow-up-rate
title: "NLS Blow Up Rate"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NLS Blow Up Rate

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/nls-blow-up-rate` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the focusing nonlinear Schrödinger equation (NLS)

$$ i\partial_t u + \Delta u + |u|^{p-1}u = 0, \qquad u(0,\cdot)=u_0, \qquad u:[0,T)\times\mathbb{R}^d\to\mathbb{C}. $$

If a solution fails to exist globally, the local theory forces $\|\nabla u(t)\|_{L^2}\to\infty$ as $t\to T$ (in the $L^2$-critical and $L^2$-supercritical ranges). The **blow-up rate problem** asks: classify the possible asymptotics of $\|\nabla u(t)\|_{L^2}$ as $t\uparrow T$, and determine which initial data produce which rate.

The central case is $L^2$-critical, $p = 1+\frac4d$ (e.g. cubic NLS in $d=2$, quintic in $d=1$), where the conjecture is a **rate dichotomy**:

> **Conjecture (blow-up dichotomy, $L^2$-critical NLS).** For $u_0\in H^1(\mathbb{R}^d)$ whose solution blows up at finite $T$, exactly one of:
> - **(log-log regime)** $\displaystyle \|\nabla u(t)\|_{L^2}\sim \Big(\frac{\log|\log (T-t)|}{T-t}\Big)^{1/2}$, and this regime is open in $H^1$ and stable;
> - **(conformal/pseudoconformal regime)** $\displaystyle \|\nabla u(t)\|_{L^2}\sim \frac{C}{T-t}$, arising on a codimension-$\ge1$ set of data;
>
> with no other rates for $H^1$ data, and in particular no rate strictly between $(T-t)^{-1/2}$ and $(T-t)^{-1}$ other than the log-log correction.

A complete resolution must (i) prove or disprove that these are the only $H^1$ rates, (ii) characterize the exceptional set, and (iii) settle the supercritical ($p>1+\frac4d$) analogue, where the conjectured generic rate is the **self-similar** one $\|\nabla u(t)\|_{L^2}\sim (T-t)^{-\sigma}$ with $\sigma=\frac12\big(\frac{2}{p-1}-\frac{d-2}{2}\big)+\frac{?}{}$ — more precisely, whether blow-up is asymptotically self-similar with the ODE/type-I scaling rather than type-II.

## 2. Mathematical Foundations

**Scaling and invariants.** The equation is invariant under $u_\lambda(t,x)=\lambda^{\frac{2}{p-1}}u(\lambda^2 t,\lambda x)$, which preserves $\dot H^{s_c}$ with $s_c=\frac d2-\frac{2}{p-1}$. Mass-critical means $s_c=0$, i.e. $p=1+\frac4d$. Conserved quantities:

$$ M(u)=\int |u|^2, \qquad E(u)=\frac12\int|\nabla u|^2-\frac{1}{p+1}\int|u|^{p+1}, \qquad P(u)=\operatorname{Im}\int \bar u\,\nabla u. $$

**Ground state.** Let $Q$ be the unique positive radial $H^1$ solution of
$$ \Delta Q - Q + Q^{p} = 0 \quad\text{on }\mathbb{R}^d, $$
(uniqueness: Kwong, 1989). In the critical case, $Q$ saturates the Gagliardo–Nirenberg inequality
$$ \|u\|_{L^{2+\frac4d}}^{2+\frac4d} \le C_{GN}\,\|u\|_{L^2}^{4/d}\|\nabla u\|_{L^2}^{2}, $$
so $E(u)\ge \frac12\|\nabla u\|_{L^2}^2\big(1-(\|u\|_{L^2}/\|Q\|_{L^2})^{4/d}\big)$, giving global existence for $\|u_0\|_{L^2}<\|Q\|_{L^2}$ (Weinstein, 1983).

**Explicit critical blow-up.** In the mass-critical case the pseudoconformal symmetry
$$ u(t,x)\mapsto \frac{1}{|t|^{d/2}}\,\bar u\!\left(\frac1t,\frac xt\right)e^{i\frac{|x|^2}{4t}} $$
maps the solitary wave $e^{it}Q(x)$ to the explicit minimal-mass blow-up solution
$$ S(t,x)=\frac{1}{|T-t|^{d/2}}\,Q\!\left(\frac{x}{T-t}\right)e^{-i\frac{|x|^2}{4(T-t)}+\frac{i}{T-t}}, \qquad \|\nabla S(t)\|_{L^2}=\frac{\|\nabla Q\|_{L^2}}{T-t}. $$

**Virial identity.** For $u_0\in\Sigma=\{u\in H^1: |x|u\in L^2\}$,
$$ \frac{d^2}{dt^2}\int |x|^2|u|^2\,dx = 8\,\big(2E(u)\big) \quad (L^2\text{-critical}), $$
so $E(u_0)<0$ forces finite-time blow-up (Glassey, 1977). This gives the lower bound $\|\nabla u(t)\|_{L^2}\gtrsim (T-t)^{-1/2}$ from the local theory (scaling of the Strichartz local existence time).

**Self-similar variables.** Writing $u(t,x)=\frac{1}{\lambda(t)^{2/(p-1)}}v(s,y)$, $y=x/\lambda(t)$, $ds/dt=\lambda^{-2}$, the profile equation for $v=Q_b$ involves the linearized operator $L=(L_+,L_-)$ around $Q$, with $L_+ = -\Delta+1-pQ^{p-1}$, $L_-=-\Delta+1-Q^{p-1}$. The log-log law emerges from the spectral gap of $L$ plus an exponentially small (in $b\sim s^{-1}$) tail radiation, governed by $\frac{db}{ds}\approx -c\,e^{-\pi/b}$.

## 3. History & State of the Art (SOTA)

- **1972–1977.** Zakharov and collaborators note self-focusing collapse in optics; Glassey's virial argument proves finite-time blow-up for negative energy data in $\Sigma$.
- **1983.** Weinstein establishes the sharp Gagliardo–Nirenberg constant and the mass threshold $\|Q\|_{L^2}$.
- **1980s–1990s.** Formal asymptotics and numerics (Landman–Papanicolaou–Sulem–Sulem, LeMesurier et al., 1988) predict the **log-log law** $\lambda(t)\sim (2\pi)^{1/2}\big((T-t)/\log|\log(T-t)|\big)^{1/2}$. The prediction was contested for a decade because of extreme numerical stiffness ($\log\log$ grows past $2$ only at astronomically small $T-t$).
- **1993.** Merle proves that minimal-mass blow-up ($\|u_0\|_{L^2}=\|Q\|_{L^2}$) is exactly $S(t)$ up to symmetries — rigidity in the conformal regime.
- **2001.** Perelman constructs, in $d=1$ quintic, a solution with the log-log rate and proves its stability in a restricted class, the first rigorous log-log result.
- **2001–2006.** **Merle–Raphaël** (Annals 2005; Invent. Math. 2004, 2006; GAFA 2003; JAMS 2006) give the definitive theory: for radial (later general) $H^1$ data with $\|Q\|_{L^2}<\|u_0\|_{L^2}<\|Q\|_{L^2}+\alpha^*$ and $E(u_0)<0$ (or small positive energy), blow-up occurs and obeys the log-log law; the set of such data is open in $H^1$; and there is a **universal upper bound** $\|\nabla u(t)\|_{L^2}\lesssim (T-t)^{-1}$ excluded in a neighborhood (no rate strictly between log-log and conformal in that mass range).
- **1997/2014.** Bourgain–Wang construct data blowing up with the conformal rate $ (T-t)^{-1}$; Merle–Raphaël–Szeftel (2013) prove these solutions are **unstable**, consistent with the codimension picture.
- **2011–2015.** Raphaël–Szeftel: minimal-mass blow-up for inhomogeneous critical NLS; Merle–Raphaël–Szeftel: constructions in the supercritical/energy-critical settings.
- **2014–2020.** Merle–Raphaël–Rodnianski, and Merle–Raphaël–Rodnianski–Szeftel (Annals 2022, on compressible fluids) develop the front/self-similar machinery that also yields new NLS-type blow-up profiles with rates $\lambda(t)\sim (T-t)^{\ell}$, $\ell>1$, in supercritical regimes.

## 4. Partial Results / Verified Cases

| Setting | Result | Reference |
|---|---|---|
| $L^2$-critical, $\|u_0\|_{L^2}=\|Q\|_{L^2}$ | Unique blow-up: $u=S(t)$ mod symmetries; rate exactly $(T-t)^{-1}$ | Merle 1993 |
| $L^2$-critical, $d\ge1$, $\|Q\|_{L^2}<\|u_0\|_{L^2}<\|Q\|_{L^2}+\alpha^*$, $E<0$ | Log-log law $\lambda(t)\sim\big(\frac{2\pi(T-t)}{\log|\log(T-t)|}\big)^{1/2}$; stable, open set | Merle–Raphaël 2003–2006 |
| Same mass window | Rate rigidity: either log-log or $\|\nabla u\|\gtrsim (T-t)^{-1}$; nothing in between | Merle–Raphaël, Annals 162 (2005) |
| $d=1$, quintic | First rigorous log-log construction with stability | Perelman 2001 |
| Conformal rate | Bourgain–Wang solutions exist; are unstable (codimension $\ge1$) | Bourgain–Wang 1997; Merle–Raphaël–Szeftel 2013 |
| $L^2$-critical, general (non-radial) $H^1$ | Blow-up for $E<0$ and localization/quantization of the $L^2$ concentration $\ge\|Q\|_{L^2}$ | Merle–Raphaël, JAMS 19 (2006) |
| Energy-critical $d=4$ radial ($p=3$) | Type-II blow-up with $\lambda(t)\sim (T-t)^{2}$ up to $\log$; discrete rate family $\lambda\sim(T-t)^{\ell}$ | Hillairet–Raphaël 2012; Merle–Raphaël–Rodnianski 2015 |
| Mass-supercritical, $s_c\in(0,1)$ | Existence of self-similar type-I blow-up numerically; rigorous constructions of $\dot H^{s_c}$-norm growth | Merle–Raphaël–Rodnianski 2015 |

Numerics confirm the log-log law only after adaptive mesh refinement down to $\lambda\sim10^{-20}$ (Sulem–Sulem's monograph reviews the discrepancy history).

## 5. Principal Obstacles

- **The log-log correction is beyond all orders.** The modulation parameter satisfies $b_s\approx -c\,e^{-\pi/b}$: the rate is driven by a term exponentially small in the expansion parameter. No finite-order perturbation theory or formal asymptotic series sees it; one needs the exact tail of the linearized resonance and matched asymptotics made rigorous with sharp weighted energy estimates.
- **Large mass is uncontrolled.** All rigidity theorems require $\|u_0\|_{L^2}<\|Q\|_{L^2}+\alpha^*$ with $\alpha^*$ small and non-explicit. Above that, multi-bubble configurations may form, and the modulation ansatz $u\approx \lambda^{-d/2}Q_b(x/\lambda)$ loses validity.
- **No monotonicity in the general case.** The virial functional $\int|x|^2|u|^2$ requires finite variance; localized virial identities generate boundary terms that are only controllable using the smallness of the excess mass.
- **Spectral input is nonperturbative.** Merle–Raphaël's proof relies on a *conjectured-then-verified* spectral property of a linearized operator, checked numerically in low dimensions and by Fibich/Merle-type arguments; extending it in $d$ and to non-radial perturbations is not routine.
- **Supercritical case lacks a variational anchor.** For $s_c>0$ there is no ground-state mass threshold; the self-similar profiles solve a nonlinear elliptic problem with complex spectral parameter and only-numerically-known existence, so even the candidate rate is not rigorously identified.

## 6. The Gap

Proven: the dichotomy inside a small mass window above $\|Q\|_{L^2}$, plus rigidity at exactly $\|Q\|_{L^2}$. Conjectured: the same dichotomy for **all** $H^1$ blow-up solutions, at arbitrary mass. The concrete missing step is a classification of the possible limits of the rescaled profile $\lambda(t)^{d/2}u(t,\lambda(t)\cdot)$ without a smallness assumption — i.e. a soliton-resolution-type statement for blow-up in $H^1$, showing the profile converges to a finite sum of ground states plus radiation, and that each bubble carries one of the two rates. Also missing: exclusion of anomalous rates such as $\lambda(t)\sim (T-t)^{1/2}|\log(T-t)|^{-\gamma}$ with $\gamma\ne 1/2$ beyond the small-mass window, and a proof that the conformal set has exactly codimension one.

## 7. Current Research (as of June 2026)

- **Modulation + monotonicity school** (Raphaël, Szeftel, Merle, Rodnianski; IHÉS, Cambridge, Courant, Princeton): pushing the log-log analysis to larger mass and to non-radial multi-bubble data; and building new type-II profiles by the "front renormalization" machinery.
- **Integrable/inverse-scattering perspective** (Zakharov school; Biondini and collaborators): for $d=1$ cubic (non-critical) and near-critical perturbations, using Riemann–Hilbert analysis to describe near-collapse structure. *(frontier — verify)*
- **Rigorous computer-assisted spectral verification** of the Merle–Raphaël spectral property in dimensions $d\le 5$ via interval arithmetic. *(frontier — verify)*
- **Constructions with prescribed non-generic rates** (Martel, Raphaël, Bahouri–Marachli-type constructions; and work on the mass-critical gKdV analogue by Martel–Merle–Raphaël, which produced the exotic $(T-t)^{-1}$-type and "exit" regimes) — these gKdV results (Acta Math. 2014; JEMS 2015) are the template being transferred back to NLS. *(frontier — verify)*
- **Multi-bubble and non-radial numerics** with adaptive rescaling to $10^{-30}$, testing whether log-log survives for masses well above $\|Q\|_{L^2}$.

## 8. Future Work

- Prove a **soliton resolution for blow-up**: $u(t)\to \sum_{j} \lambda_j^{-d/2}Q(\cdot/\lambda_j)e^{i\gamma_j} + u^*$ near $T$, in $H^1$, with no mass restriction.
- Remove the smallness $\alpha^*$ by combining the log-log monotonicity with a Kenig–Merle concentration–compactness/rigidity scheme.
- Establish that the Bourgain–Wang manifold is a genuine codimension-one $C^1$ manifold separating log-log blow-up from global scattering (partial: Merle–Raphaël–Szeftel 2013).
- Settle existence of exactly self-similar profiles in the mass-supercritical range $0<s_c<1$, and prove type-I rate $\|\nabla u\|\sim (T-t)^{-\frac{1-s_c}{2}}$ for generic supercritical data.
- Transfer the gKdV "exit regime" classification (Martel–Merle–Raphaël) to NLS to describe the boundary between blow-up and scattering.

## 9. Key References

- **[Foundational]** M. I. Weinstein. *Nonlinear Schrödinger equations and sharp interpolation estimates.* Communications in Mathematical Physics **87** (1983), 567–576.
- **[Foundational]** R. T. Glassey. *On the blowing up of solutions to the Cauchy problem for nonlinear Schrödinger equations.* Journal of Mathematical Physics **18** (1977), 1794–1797.
- **[Foundational]** F. Merle. *Determination of blow-up solutions with minimal mass for nonlinear Schrödinger equations with critical power.* Duke Mathematical Journal **69** (1993), 427–454.
- **[Foundational]** M. K. Kwong. *Uniqueness of positive solutions of $\Delta u-u+u^p=0$ in $\mathbb{R}^n$.* Archive for Rational Mechanics and Analysis **105** (1989), 243–266.
- **[SOTA]** F. Merle, P. Raphaël. *On universality of blow-up profile for $L^2$ critical nonlinear Schrödinger equation.* Inventiones Mathematicae **156** (2004), 565–672.
- **[SOTA]** F. Merle, P. Raphaël. *The blow-up dynamic and upper bound on the blow-up rate for critical nonlinear Schrödinger equation.* Annals of Mathematics **161** (2005), 157–222.
- **[SOTA]** F. Merle, P. Raphaël. *Sharp upper bound on the blow-up rate for the critical nonlinear Schrödinger equation.* Geometric and Functional Analysis **13** (2003), 591–642.
- **[SOTA]** F. Merle, P. Raphaël. *Profiles and quantization of the blow up mass for critical nonlinear Schrödinger equation.* Communications in Mathematical Physics **253** (2005), 675–704.
- **[SOTA]** F. Merle, P. Raphaël, J. Szeftel. *On collapsing ring blow-up solutions to the mass supercritical NLS.* Duke Mathematical Journal **163** (2014), 369–431.
- **[SOTA]** F. Merle, P. Raphaël, J. Szeftel. *The instability of Bourgain–Wang solutions for the $L^2$ critical NLS.* American Journal of Mathematics **135** (2013), 967–1017.
- **[Recent]** F. Merle, P. Raphaël, I. Rodnianski. *Type II blow up for the energy supercritical NLS.* Cambridge Journal of Mathematics **3** (2015), 439–617.
- **[Related]** G. Perelman. *On the formation of singularities in solutions of the critical nonlinear Schrödinger equation.* Annales Henri Poincaré **2** (2001), 605–673.
- **[Related]** J. Bourgain, W. Wang. *Construction of blowup solutions for the nonlinear Schrödinger equation with critical nonlinearity.* Annali della Scuola Normale Superiore di Pisa **25** (1997), 197–215.
- **[Survey]** C. Sulem, P.-L. Sulem. *The Nonlinear Schrödinger Equation: Self-Focusing and Wave Collapse.* Applied Mathematical Sciences 139, Springer, 1999.
- **[Survey]** T. Cazenave. *Semilinear Schrödinger Equations.* Courant Lecture Notes 10, AMS, 2003.
- **[Survey]** P. Raphaël. *On the singularity formation for the nonlinear Schrödinger equation.* Clay Mathematics Proceedings, Vol. 17 (Evolution Equations), AMS, 2013.

## 10. Worked Example / Concrete Special Case

**Setting:** $d=2$, cubic focusing NLS $i\partial_t u+\Delta u+|u|^2u=0$ ($p=3=1+\frac4d$, mass-critical).

**Step 1 — the ground state.** $Q$ solves $\Delta Q-Q+Q^3=0$ on $\mathbb{R}^2$, radial, positive, unique. Numerically $\|Q\|_{L^2}^2\approx 1.8623$ ("Townes soliton" power). The Pohozaev identities give, in $d=2$,
$$ \int|\nabla Q|^2=\int Q^2=\tfrac12\int Q^4, \qquad\text{hence } E(Q)=\tfrac12\int|\nabla Q|^2-\tfrac14\int Q^4=0. $$
So the solitary wave $e^{it}Q$ has exactly zero energy — the borderline that makes $d=2$ cubic critical.

**Step 2 — explicit conformal blow-up.** Apply the pseudoconformal transform with $T=1$:
$$ S(t,x)=\frac{1}{1-t}\,Q\!\Big(\frac{x}{1-t}\Big)\exp\Big(-i\frac{|x|^2}{4(1-t)}+\frac{i}{1-t}\Big). $$
Then $\|S(t)\|_{L^2}=\|Q\|_{L^2}$ for all $t$ (mass is scale-invariant in $d=2$ with this scaling), while
$$ \|\nabla S(t)\|_{L^2}=\frac{\|\nabla Q\|_{L^2}}{1-t}\xrightarrow[t\to1^-]{}\infty. $$
By Merle's 1993 theorem this is the *only* blow-up solution at mass exactly $\|Q\|_{L^2}$.

**Step 3 — perturb to get log-log.** Take $u_0=(1+\varepsilon)Q$ with $0<\varepsilon\ll1$. Mass: $\|u_0\|_{L^2}^2=(1+\varepsilon)^2\|Q\|_{L^2}^2>\|Q\|_{L^2}^2$, just above threshold. Energy, using $E(Q)=0$ and homogeneity:
$$ E((1+\varepsilon)Q)=\frac{(1+\varepsilon)^2}{2}\int|\nabla Q|^2-\frac{(1+\varepsilon)^4}{4}\int Q^4 = \int|\nabla Q|^2\Big(\frac{(1+\varepsilon)^2}{2}-\frac{(1+\varepsilon)^4}{2}\Big)<0. $$
Negative energy plus finite variance $\Rightarrow$ blow-up in finite time $T<\infty$ by Glassey's virial identity $\frac{d^2}{dt^2}\int|x|^2|u|^2=16E(u_0)<0$. And since $\varepsilon$ small puts the data in the Merle–Raphaël window $\|Q\|_{L^2}<\|u_0\|_{L^2}<\|Q\|_{L^2}+\alpha^*$, the rate is **log-log**, not conformal:
$$ \|\nabla u(t)\|_{L^2}\sim \frac{\|\nabla Q\|_{L^2}}{\lambda(t)},\qquad \lambda(t)\sim\sqrt{\frac{2\pi (T-t)}{\log|\log(T-t)|}}. $$

**Step 4 — why this is hard to see numerically.** At $T-t=10^{-10}$, $\log|\log(T-t)|=\log(23.0)\approx 3.14$; at $T-t=10^{-100}$ it is only $\approx 5.4$. The log-log factor moves by a factor $1.7$ over 90 decades. Any simulation truncated at moderate resolution reads the rate as $\approx (T-t)^{-1/2}$ times a slowly-drifting constant — which is precisely why the law was disputed from 1988 until the Merle–Raphaël proofs.

**Takeaway.** Mass $=\|Q\|_{L^2}$ gives rate $(T-t)^{-1}$; mass $=\|Q\|_{L^2}+\delta$ with $\delta$ small gives $\big(\frac{\log|\log(T-t)|}{T-t}\big)^{1/2}$. The open problem is everything at mass $\ge \|Q\|_{L^2}+\alpha^*$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*