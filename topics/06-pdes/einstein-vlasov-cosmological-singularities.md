---
id: 06-pdes/einstein-vlasov-cosmological-singularities
title: "Einstein-Vlasov System Cosmological Singularities"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Einstein-Vlasov System Cosmological Singularities

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/einstein-vlasov-cosmological-singularities` · **Status:** open

## 1. Problem Statement / Conjecture

Determine the structure of the past (Big Bang) singularity for generic solutions of the Einstein–Vlasov system on cosmological (spatially compact) spacetimes, and prove strong cosmic censorship in that class.

Two linked claims:

**(A) Singularity structure.** For generic initial data on a compact Cauchy surface $\Sigma$, the maximal globally hyperbolic development $(M,g,f)$ is past-incomplete, the Kretschmann scalar $R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta}$ blows up along every past-inextendible causal geodesic, and the asymptotics are described by the BKL picture: local, spatially decoupled, oscillatory (Mixmaster) Kasner epochs, with the Vlasov matter asymptotically negligible relative to the shear.

**(B) Strong cosmic censorship (SCC).** For a generic set of data, the maximal development is inextendible as a Lorentzian manifold of regularity $C^2$ (ideally $C^0$), so the evolution is deterministic.

A complete solution of (A) requires either a proof of BKL-type asymptotics for an open (or generic) set of data without symmetry, or a counterexample; a complete solution of (B) requires a precise genericity notion (open dense, or complement of a set of "infinite codimension") together with the inextendibility proof. Both are open. Neither restricted symmetry classes nor the small-data quiescent regime settles them.

## 2. Mathematical Foundations

Let $(M,g)$ be a $4$-dimensional time-oriented Lorentzian manifold, signature $(-,+,+,+)$. Particles of mass $m\ge 0$ move on the mass shell
$$P_m=\{(x,p)\in TM:\ g_{\alpha\beta}(x)p^\alpha p^\beta=-m^2,\ p \text{ future-directed}\}.$$
The particle density $f:P_m\to[0,\infty)$ satisfies the **Vlasov (collisionless Boltzmann) equation**, i.e. $f$ is constant along the geodesic spray:
$$p^\alpha\frac{\partial f}{\partial x^\alpha}-\Gamma^{\alpha}_{\ \beta\gamma}(x)\,p^\beta p^\gamma\frac{\partial f}{\partial p^\alpha}=0 .$$
In a chart with $p^0$ determined by the mass shell, the energy–momentum tensor is
$$T_{\alpha\beta}(x)=\int_{\mathbb{R}^3} f(x,p)\,p_\alpha p_\beta\,\frac{\sqrt{|\det g|}}{-p_0}\,dp^1dp^2dp^3 ,$$
and the system closes with
$$G_{\alpha\beta}=R_{\alpha\beta}-\tfrac12 R\,g_{\alpha\beta}=8\pi T_{\alpha\beta}.$$
$T_{\alpha\beta}$ is divergence-free precisely because $f$ solves the Vlasov equation. If $f\ge0$ has compact momentum support, $T$ satisfies the dominant and strong energy conditions, so the Hawking–Penrose singularity theorems apply: a compact Cauchy surface with mean curvature bounded away from zero gives past geodesic incompleteness.

**Kasner backgrounds.** The vacuum Bianchi I solutions
$$g=-dt^2+\sum_{i=1}^3 t^{2p_i}(dx^i)^2,\qquad \sum_i p_i=\sum_i p_i^2=1,$$
form the Kasner circle $\mathcal{K}$; $t\to0^+$ is a curvature singularity except at the flat points $p=(1,0,0)$ and permutations (Taub points). BKL asserts that a generic cosmological singularity is, pointwise in space, an infinite chaotic sequence of Kasner epochs joined by curvature-driven Kasner transitions, matter becoming dynamically irrelevant. The competing **quiescent** (AVTD, asymptotically velocity term dominated) regime holds when the exponents lie in a subcritical range and oscillations are suppressed — e.g. a stiff fluid or scalar field.

**Formulation.** In CMC-harmonic or constant-areal gauge the coupled system is a quasilinear hyperbolic system for $g$ plus a transport equation for $f$ on a $7$-dimensional phase space; well-posedness in $H^s$, $s>3/2$, with continuation criteria controlling momentum support, is classical (Choquet-Bruhat; Rendall).

## 3. History & State of the Art (SOTA)

- **1970** — Belinskii, Khalatnikov, Lifshitz propose the oscillatory approach to a general cosmological singularity (*Adv. Phys.* 19).
- **1990s** — Rendall initiates the rigorous PDE study of Einstein–Vlasov cosmologies: crushing singularities and global CMC foliations for spherically, plane and hyperbolically symmetric solutions (1995); Rein (1996) proves global existence in areal time for these symmetry classes.
- **1996** — Rendall shows Bianchi I Einstein–Vlasov solutions with reflection-symmetric distribution functions have velocity-dominated (Kasner-like) past asymptotics.
- **1999–2006** — Rendall–Tod and Rendall–Uggla analyse LRS Bianchi models; Heinzle–Uggla give the Hubble-normalized dynamical-systems treatment of Bianchi I Vlasov, isolating the Taub points as the degenerate directions where the Vlasov energy density is not asymptotically negligible.
- **2001** — Ringström's Bianchi IX attractor theorem: generic vacuum Bianchi IX solutions oscillate on the Kasner circle. Vlasov matter is expected (not proved) not to change this.
- **2005–2016** — Dafermos–Rendall prove $C^2$-inextendibility for expanding surface-symmetric Vlasov cosmologies (2005) and SCC for surface-symmetric cosmological spacetimes with collisionless matter (*CPAM*, 2016).
- **2013–2016** — Future-direction results: Ringström's future stability of accelerated expansion with Vlasov matter; Andréasson–Ringström prove cosmic no-hair in the $T^3$-Gowdy Einstein–Vlasov setting.
- **2018–2023** — Rodnianski–Speck and Fournodavlos–Rodnianski–Speck establish stable Big Bang formation for the Einstein–scalar-field / stiff-fluid systems in the complete subcritical regime. No Vlasov analogue exists: Vlasov matter is *not* stiff and does not enforce quiescence.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| Bianchi I, massive/massless, reflection-symmetric $f$ | Past asymptotics are velocity-dominated; convergence to a point of $\mathcal{K}$ (Rendall 1996) |
| Bianchi I, general $f$ | Hubble-normalized past attractor contained in $\mathcal{K}$; Taub points degenerate (Heinzle–Uggla 2006) |
| LRS Bianchi types I, II, III, and Kantowski–Sachs | Complete past and future asymptotics (Rendall–Tod 1999; Rendall–Uggla 2000) |
| Spherical ($k=1$), plane ($k=0$), hyperbolic ($k=-1$) surface symmetry | Global areal foliation, crushing singularity $\mathrm{tr}\,K\to-\infty$ (Rendall 1995; Rein 1996) |
| Surface-symmetric cosmologies, $k=0,-1$ | Strong cosmic censorship, $C^2$-inextendibility (Dafermos–Rendall, CPAM 2016) |
| $T^2$-symmetric | SCC established under the symmetry hypotheses (Dafermos–Rendall, 2006 preprint) |
| $T^3$-Gowdy symmetric, $\Lambda>0$ | Cosmic no-hair; future asymptotics (Andréasson–Ringström, JEMS 2016) |
| Small data near FLRW, $\Lambda>0$ or expanding | Future global existence and stability (Ringström 2013; Fajman and collaborators) |

Nothing is known for generic data without symmetry in the past direction beyond the singularity theorems.

## 5. Principal Obstacles

- **No quiescence mechanism.** The subcritical Kasner regime is enforced by a stiff fluid or scalar field ($c_s=1$), which pushes the Kasner exponents into the AVTD range. Vlasov matter has $0\le p\le\rho/3$ with anisotropic pressures and produces no such shift; the expected asymptotics are the *oscillatory* BKL ones, for which no PDE technique controls an infinite chain of transitions.
- **Momentum-space anisotropy.** The Vlasov stress $T_{ij}$ depends on the full momentum profile, not on $\rho$ alone. Near a Kasner state with exponent $p_i\to1$, momenta along $x^i$ are not redshifted away and the matter contribution stops being negligible; the "matter is irrelevant near the singularity" heuristic fails precisely at the Taub points that BKL transitions pass near.
- **Loss of hyperbolic estimates.** Energy methods for quasilinear wave systems require a uniform hierarchy of blow-up rates. Oscillation destroys any fixed hierarchy; each Kasner epoch has different exponents, so no single weighted norm is monotone.
- **Coupling of transport and geometry.** Vlasov characteristics are the geodesics of the very metric being estimated; near a singularity, momentum support grows without bound and the standard continuation criterion (bounded $p$-support) is unavailable.
- **Genericity is undefined.** For SCC one must exclude a set of data of "infinite codimension" (Ringström's formulation in the Gowdy case); there is no general framework for such statements without symmetry.

## 6. The Gap

Proven: (i) singularity formation (incompleteness) from energy conditions; (ii) precise asymptotics in symmetry classes whose reduced dynamics is finite-dimensional or $1+1$; (iii) stable Big Bang formation for *stiff* matter without symmetry.

Conjectured: BKL asymptotics and SCC for generic data with Vlasov matter and no symmetry.

The exact barrier: constructing a stable, spatially local, oscillatory Kasner regime — i.e. an open set of data whose development undergoes infinitely many Kasner transitions with the Vlasov contribution provably subdominant — and showing that the Vlasov stress does not destabilize the transitions near the Taub points. Even a rigorous *single* curvature-driven Kasner transition with Vlasov matter and no symmetry is not available.

## 7. Current Research (as of June 2026)

- **Vienna (Fajman and collaborators).** Stability of cosmological spacetimes with kinetic matter, both directions of time; work on Kasner-like singularities coupled to Vlasov matter *(frontier — verify)*.
- **Princeton / MIT / Vanderbilt (Rodnianski, Speck, Fournodavlos, Luk).** Extending the subcritical Big Bang machinery beyond scalar fields; asymptotically Kasner-like singularities and their stability.
- **KTH (Ringström).** Wave equations on silent big-bang backgrounds and the associated asymptotic classification, a proposed route to the Vlasov case *(frontier — verify)*.
- **Gothenburg / Chalmers (Andréasson).** Symmetric Einstein–Vlasov cosmologies and numerics.
- **Karlstad / Heinzle (Uggla, Heinzle).** Dynamical-systems and Hubble-normalized formulations, including "cosmological billiards" with anisotropic matter.

## 8. Future Work

1. Prove a rigorous single Kasner (Taub) transition in Bianchi II Einstein–Vlasov with general $f$, then chain transitions as in Ringström's vacuum Bianchi IX attractor argument.
2. Identify a sharp condition on the momentum support of $f$ under which past asymptotics are velocity-dominated, generalizing Rendall's reflection-symmetry hypothesis.
3. Construct AVTD Big Bang solutions with Vlasov matter and *no* symmetry via Fuchsian methods (Andersson–Rendall style), even if non-generic.
4. Settle $C^0$-inextendibility in the symmetry classes where $C^2$-SCC is known.
5. Develop numerics resolving spatially inhomogeneous Vlasov singularities to test whether matter remains subdominant.

## 9. Key References

- **[Foundational]** V. A. Belinskii, I. M. Khalatnikov, E. M. Lifshitz. *Oscillatory approach to a singular point in the relativistic cosmology.* Advances in Physics 19 (1970), 525–573.
- **[Foundational]** A. D. Rendall. *Crushing singularities in spacetimes with spherical, plane and hyperbolic symmetry.* Classical and Quantum Gravity 12 (1995), 1517–1533.
- **[Foundational]** G. Rein. *Cosmological solutions of the Vlasov–Einstein system with spherical, plane and hyperbolic symmetry.* Mathematical Proceedings of the Cambridge Philosophical Society 119 (1996), 739–762.
- **[Foundational]** A. D. Rendall. *The initial singularity in solutions of the Einstein–Vlasov system of Bianchi type I.* Journal of Mathematical Physics 37 (1996), 438–451.
- **[Structural]** A. D. Rendall, K. P. Tod. *Dynamics of spatially homogeneous solutions of the Einstein–Vlasov equations which are locally rotationally symmetric.* Classical and Quantum Gravity 16 (1999), 1705–1726.
- **[Structural]** H. Ringström. *The Bianchi IX attractor.* Annales Henri Poincaré 2 (2001), 405–500.
- **[Structural]** J. M. Heinzle, C. Uggla. *Dynamics of the spatially homogeneous Bianchi type I Einstein–Vlasov equations.* Classical and Quantum Gravity 23 (2006), 3463–3490.
- **[SOTA]** M. Dafermos, A. D. Rendall. *Strong cosmic censorship for surface-symmetric cosmological spacetimes with collisionless matter.* Communications on Pure and Applied Mathematics 69 (2016), 815–908.
- **[SOTA]** H. Andréasson, H. Ringström. *Proof of the cosmic no-hair conjecture in the $T^3$-Gowdy symmetric Einstein–Vlasov setting.* Journal of the European Mathematical Society 18 (2016), 1565–1650.
- **[SOTA]** G. Fournodavlos, I. Rodnianski, J. Speck. *Stable Big Bang formation for Einstein's equations: the complete sub-critical regime.* Journal of the American Mathematical Society 36 (2023), 827–916.
- **[SOTA]** I. Rodnianski, J. Speck. *Stable Big Bang formation in near-FLRW solutions to the Einstein–scalar field and Einstein–stiff fluid systems.* Selecta Mathematica 24 (2018), 4293–4459.
- **[Book]** H. Ringström. *On the Topology and Future Stability of the Universe.* Oxford University Press, 2013.
- **[Survey]** H. Andréasson. *The Einstein–Vlasov System / Kinetic Theory.* Living Reviews in Relativity 14 (2011), 4.
- **[Survey]** H. Ringström. *Cosmic censorship for Gowdy spacetimes.* Living Reviews in Relativity 13 (2010), 2.

## 10. Worked Example / Concrete Special Case

**Bianchi I with a single momentum direction.** Take
$$g=-dt^2+\sum_{i=1}^3 a_i(t)^2 (dx^i)^2 .$$
Since $g$ is $x$-independent, the covariant momenta $v_i=p_i$ are constants of motion, so $f(t,v)=f_0(v)$. With $m=0$,
$$p^0=\Big(\textstyle\sum_j v_j^2/a_j^2\Big)^{1/2},\qquad
\rho=\frac{1}{a_1a_2a_3}\int f_0(v)\Big(\sum_j \frac{v_j^2}{a_j^2}\Big)^{1/2}dv,\quad
P_i=\frac{1}{a_1a_2a_3}\int f_0(v)\,\frac{v_i^2/a_i^2}{\big(\sum_j v_j^2/a_j^2\big)^{1/2}}\,dv .$$

Concentrate $f_0$ on $v=(V,0,0)$ (formal null dust along $x^1$):
$$\rho=\frac{V}{a_1^2\,a_2a_3},\qquad P_1=\rho,\quad P_2=P_3=0 .$$

Evaluate on a Kasner background $a_i=t^{p_i}$, $\sum p_i=\sum p_i^2=1$, for which $H=\dot V_{\rm vol}/(3V_{\rm vol})=1/(3t)$ and the shear energy density scales as $t^{-2}$:
$$\rho \;\propto\; t^{-(1+p_1)},\qquad
\Omega:=\frac{8\pi\rho}{3H^2}\;\propto\;t^{\,1-p_1}.$$

Because $p_1\le 1$ always, $\Omega\to0$ as $t\to0^+$ for every Kasner state with $p_1<1$: **the matter is asymptotically negligible and the singularity is Kasner-like**, matching Rendall (1996). The single exception is the Taub point $p=(1,0,0)$, where $1-p_1=0$ and $\Omega$ does not decay — the Vlasov stress stays at the same order as the shear.

The consequence for the open problem: a distribution $f_0$ with momenta in all three directions makes each of the three Taub points marginal in the same way. BKL transitions in Bianchi VIII/IX drive the state arbitrarily close to Taub points infinitely often, so the "matter is irrelevant" estimate degenerates on every epoch of the oscillation. Controlling that degeneracy uniformly along an infinite chain of transitions — already unproved in Bianchi IX, let alone without symmetry — is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*