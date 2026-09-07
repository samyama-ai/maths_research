---
id: 06-pdes/lake-equations-global-regularity
title: "Lake Equations Global Regularity"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lake Equations Global Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/lake-equations-global-regularity` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The *lake equations* are the rigid-lid, zero-Froude-number limit of the 3D incompressible Euler equations in a shallow basin of depth $b(x)$. On a bounded planar domain $\Omega \subset \mathbb{R}^2$ they read

$$\partial_t v + (v\cdot\nabla)v + \nabla p = 0,\qquad \nabla\cdot(b\,v)=0,\qquad (b\,v)\cdot n\big|_{\partial\Omega}=0 .$$

**Question.** For which classes of depth functions $b \ge 0$ and initial data does the Cauchy problem have a *global, unique* weak solution, and for which does that solution stay as regular as the data?

The problem is partially solved. Global existence and uniqueness are theorems when $b$ is smooth and bounded away from zero (Levermore–Oliver–Titi 1996), and when $b$ degenerates at the shore like a power of the distance to $\partial\Omega$ (Bresch–Métivier 2006; Lacave–Nguyen–Pausader 2014). It is open in three regimes:

1. **Rough topography.** $b \in L^\infty$ with $0 < b_- \le b \le b_+$ but $b \notin W^{1,\infty}$, or $b$ of bounded variation (a lake with a sharp underwater ledge).
2. **Interior degeneracy.** $b$ vanishing at an interior point or on an interior curve (a shoal or an emergent island), where $b^{-1}$ is unbounded inside the flow domain.
3. **Low-integrability vorticity.** Uniqueness for potential vorticity $q_0 \in L^p$, $p < \infty$ — the lake analogue of the Yudovich uniqueness gap for 2D Euler.

A complete solution means either a global well-posedness theorem covering these classes, or an explicit example of finite-time loss of uniqueness or of regularity.

## 2. Mathematical Foundations

Let $\Omega \subset \mathbb{R}^2$ be bounded, simply connected, with $C^{2}$ (or Lipschitz) boundary, and $b:\overline\Omega \to [0,\infty)$ the depth.

**Stream function.** The anelastic constraint $\nabla\cdot(bv)=0$ with no flux gives $bv = \nabla^\perp\psi$, $\nabla^\perp = (-\partial_2,\partial_1)$, with $\psi|_{\partial\Omega}=0$. Hence

$$v = \frac{1}{b}\nabla^\perp\psi .$$

**Potential vorticity.** With $\omega = \nabla^\perp \cdot v = \partial_1 v_2 - \partial_2 v_1$, set

$$q := \frac{\omega}{b}.$$

Taking the curl of the momentum equation eliminates $p$ and yields the transport law

$$\partial_t q + v\cdot\nabla q = 0, \qquad v=\frac{1}{b}\nabla^\perp\psi, \qquad \nabla\cdot\!\left(\frac{1}{b}\nabla\psi\right) = b\,q .$$

This is the exact structural analogue of 2D Euler ($b\equiv 1$), except that the Laplacian is replaced by the **degenerate/singular elliptic operator** $L_b \psi := \nabla\cdot(b^{-1}\nabla\psi)$, whose coefficient $b^{-1}$ blows up wherever the lake dries out.

**Conserved quantities.** For smooth solutions,

$$E(t)=\tfrac12\int_\Omega b\,|v|^2\,dx = \tfrac12\int_\Omega \frac{|\nabla\psi|^2}{b}\,dx, \qquad \int_\Omega b\,f(q)\,dx \quad \text{for every } f \in C^1 ,$$

are constant in time; in particular $\|q(t)\|_{L^p(b\,dx)} = \|q_0\|_{L^p(b\,dx)}$ for all $p\in[1,\infty]$.

**Natural function spaces.** The energy space is the weighted space $H^1_{1/b}(\Omega) = \{\psi:\ \int b^{-1}|\nabla\psi|^2<\infty,\ \psi|_{\partial\Omega}=0\}$. If $b(x) \simeq d(x)^a$ with $d(x)=\operatorname{dist}(x,\partial\Omega)$, the weight is $d^{-a}$.

**Derivation and companions.** The lake system is the leading order of an asymptotic expansion in the aspect ratio $\varepsilon = (\text{depth})/(\text{horizontal scale})$ at fixed rigid lid; the $O(\varepsilon^2)$ correction is the **great lake equations**, with a modified (nonlocal, dispersive) relation between velocity and momentum (Camassa–Holm–Levermore 1996, 1997).

## 3. History & State of the Art (SOTA)

- **1996 — derivation.** Camassa, Holm and Levermore derived the lake and great lake models by variational asymptotics from the shallow-water/Euler system with varying bottom (*Physica D* 98, 258–286).
- **1996 — global well-posedness, nondegenerate case.** Levermore, Oliver and Titi proved global existence and uniqueness for the lake and great lake equations when $b \in C^2(\overline\Omega)$ and $b \ge b_- > 0$, for $q_0 \in L^\infty$ (*Indiana Univ. Math. J.* 45, 479–510). The proof is a Yudovich argument: $\|q(t)\|_\infty=\|q_0\|_\infty$, elliptic regularity for $L_b$ gives $v$ log-Lipschitz, and the flow map is unique with an Osgood modulus.
- **1996 — vanishing shoreline, first results.** Levermore, Oliver and Titi extended global well-posedness to depths vanishing at the shore under regularity/nondegeneracy hypotheses on $b$ (*Physica D* 98, 492–509).
- **2006 — degenerate elliptic breakthrough.** Bresch and Métivier proved global existence and uniqueness for topographies vanishing at the boundary like $d^a$, covering the physically natural sloping beach, by establishing new $W^{2,p}$-type estimates for $L_b$ in weighted spaces (*Nonlinearity* 19, 591–610).
- **2014 — topography sensitivity.** Lacave, Nguyen and Pausader treated general degeneracy exponents and studied stability of solutions under perturbation of $b$, including whether islands can be created or removed in the limit (*J. Math. Fluid Mech.* 16, 375–406).
- **2020 — vortex dynamics.** Dekeyser and Van Schaftingen constructed desingularized concentrated vortices and derived their point-vortex law $\dot{x} = \tfrac12 \nabla^\perp \log b(x) \cdot \Gamma + \dots$, showing that topography, not just the domain, drives vortex drift (*Comm. Math. Phys.* 375, 1459–1501).

Computationally, the lake equations are standard in geophysical fluid dynamics as the rigid-lid barotropic model; no numerical study has produced evidence of singularity formation for bounded $q_0$.

## 4. Partial Results / Verified Cases

| Class of $b$ | Data | Result |
|---|---|---|
| $b\in C^2(\overline\Omega)$, $b\ge b_->0$ | $q_0\in L^\infty$ | Global existence + uniqueness (Levermore–Oliver–Titi 1996) |
| Same | $q_0 \in C^{k,\alpha}$ | Global persistence of regularity; double-exponential growth bound $\|\nabla q(t)\|_\infty \le C\exp(\exp(Ct))$, inherited from 2D Euler |
| Great lake equations, $b\ge b_->0$ smooth | smooth data | Global well-posedness (Levermore–Oliver–Titi 1996) |
| $b \simeq d^a$ at $\partial\Omega$, $a>0$, $b>0$ inside | $q_0\in L^\infty$ | Global existence + uniqueness (Bresch–Métivier 2006; extended in Lacave–Nguyen–Pausader 2014) |
| $b^{-1}$ an $A_2$ Muckenhoupt weight (holds for $a<1$) | $q_0 \in L^\infty$ | Elliptic theory of Fabes–Kenig–Serapioni applies directly; classical Yudovich scheme closes |
| Radially symmetric $b$, radial $q_0$ | any $q_0 \in L^1_{loc}$ | Explicitly solvable, stationary (see §10) |
| Any admissible $b$, $q_0 \in L^p$, $p>1$ | — | Global *existence* of weak solutions by compactness; **uniqueness unknown** |

Uniqueness of energy-class weak solutions with $q_0 \in L^\infty$ is thus known in every regime where the elliptic estimate $\|\nabla \psi / b\|_{LL} \lesssim \|q\|_{L^\infty}$ (log-Lipschitz) has been proven.

## 5. Principal Obstacles

- **The velocity is a quotient, not a gradient.** $v = b^{-1}\nabla^\perp\psi$. Boundedness of $v$ near a dry shore requires the *cancellation* $|\nabla\psi| = O(b)$, which is not delivered by any generic elliptic estimate — it must be extracted from the structure of $L_b\psi = bq$ (the right-hand side also vanishes). Standard Calderón–Zygmund theory for uniformly elliptic operators is unavailable because $b^{-1}\to\infty$.
- **Muckenhoupt failure.** For $b\simeq d^a$, the weight $d^{-a}$ belongs to $A_2$ exactly when $a<1$. For $a \ge 1$ — including the linear beach $a=1$ — the degenerate-elliptic Harnack/Hölder theory of Fabes–Kenig–Serapioni does not apply, and each new exponent range has needed hand-built weighted estimates.
- **Interior zeros are qualitatively worse than boundary zeros.** If $b(x_0)=0$ at an interior point, the level set $\{b=0\}$ is not a barrier the flow respects: trajectories can approach it, and $\|q\|_{L^\infty(b\,dx)}$ controls nothing near $x_0$ since the measure $b\,dx$ degenerates there. The transport argument loses its conserved quantity precisely where the elliptic problem is worst.
- **Yudovich's argument is not scale-invariantly improvable.** As for 2D Euler, uniqueness for $q_0\in L^p$, $p<\infty$, fails to follow because $v$ is then only in a Sobolev class where DiPerna–Lions/Ambrosio theory gives a unique *regular Lagrangian flow* but not uniqueness of the nonlinear PDE. Non-uniqueness constructions by convex integration for 2D Euler in low-regularity classes suggest the answer for lakes may be negative, but they do not currently respect the constraint $\nabla\cdot(bv)=0$ with variable $b$.
- **No self-similar or scaling structure.** Variable $b$ destroys the scaling symmetry that underwrites blow-up analyses for other 2D transport-elliptic systems (e.g. SQG), so the standard scenario-based machinery has no starting point.

## 6. The Gap

Everything proven rests on one implication:

$$q \in L^\infty \ \Longrightarrow\ v=\tfrac1b\nabla^\perp\psi \ \text{log-Lipschitz} \ \Longrightarrow\ \text{unique Osgood flow}.$$

The gap is exactly the first arrow outside the two settings where it is known ($b$ bounded below; $b\simeq d^a$ at the shore with $b>0$ inside). Concretely, the missing step is a bound of the form

$$\left\| \frac{\nabla \psi}{b} \right\|_{L^\infty} + \sup_{|x-y|<\tfrac12} \frac{|v(x)-v(y)|}{|x-y|\,\bigl(1+\log\frac{1}{|x-y|}\bigr)} \ \le\ C(b)\,\|q\|_{L^\infty},$$

valid for $b$ merely bounded measurable with an interior zero, or for $b\in BV$ with a jump. No known technique produces the required cancellation between the degeneracy of the coefficient $b^{-1}$ and the degeneracy of the source $bq$ without pointwise control on $\nabla b$.

## 7. Current Research (as of June 2026)

- **Degenerate elliptic regularity.** Continuation of the Bresch–Métivier program: sharp weighted $W^{2,p}$ and Schauder theory for $\nabla\cdot(d^{-a}\nabla \cdot)$ across the $A_2$ threshold $a=1$, in Lipschitz and corner domains (French schools around Grenoble/Rennes, and the Lyon PDE group).
- **Singular topography and islands.** Lacave and collaborators (Grenoble) on the limit of lake flows as an island shrinks to a point, and on flows past emerging shoals — the natural bridge to 2D Euler on singular domains. *(frontier — verify)* Preprints treating $b$ vanishing on an interior curve claim existence but not uniqueness.
- **Vortex dynamics and desingularization.** Following Dekeyser–Van Schaftingen, work on stability of vortex pairs and on long-time confinement of vorticity in lakes with nonconstant $b$ (Louvain, Torino).
- **Convex-integration non-uniqueness.** Adaptation of 2D Euler non-uniqueness schemes to anelastic constraints; the obstruction is building Mikado/Beltrami-type building blocks compatible with $\nabla\cdot(bv)=0$. *(frontier — verify)*
- **Great lake equations at degenerate shores.** Global well-posedness of the $O(\varepsilon^2)$ model when the depth vanishes is open even for $a=1$; the dispersive correction destroys the exact transport of $q$.

## 8. Future Work

- Prove or disprove the log-Lipschitz estimate for $b \in L^\infty$ with $0<b_-\le b\le b_+$ but no derivative control — this would settle the "ledge" case and is the most tractable open item.
- Construct a lake with an interior zero and $q_0 \in L^\infty$ for which two distinct energy-class solutions exist; this is the most likely route to a *negative* answer.
- Extend the theory to the great lake equations with degenerate shorelines, using the variational (Euler–Poincaré) structure from Camassa–Holm–Levermore in place of vorticity transport.
- Quantify $\|\nabla q(t)\|_{L^\infty}$ growth: is the double-exponential 2D Euler bound attained for some $b$, and does topography accelerate filamentation?
- Establish the vanishing-viscosity limit for the viscous lake system on a degenerate domain, where a boundary layer forms at the drying shore.

## 9. Key References

- **[Foundational]** R. Camassa, D. D. Holm, C. D. Levermore. *Long-time effects of bottom topography in shallow water.* Physica D **98** (1996), 258–286.
- **[Foundational]** R. Camassa, D. D. Holm, C. D. Levermore. *Long-time shallow-water equations with a varying bottom.* Journal of Fluid Mechanics **349** (1997), 173–189.
- **[Foundational]** C. D. Levermore, M. Oliver, E. S. Titi. *Global well-posedness for models of shallow water in a basin with a varying bottom.* Indiana University Mathematics Journal **45** (1996), 479–510.
- **[Foundational]** C. D. Levermore, M. Oliver, E. S. Titi. *Global well-posedness for the lake equations.* Physica D **98** (1996), 492–509.
- **[SOTA]** D. Bresch, G. Métivier. *Global existence and uniqueness for the lake equations with vanishing topography: elliptic estimates for degenerate equations.* Nonlinearity **19** (2006), 591–610.
- **[SOTA]** C. Lacave, T. T. Nguyen, B. Pausader. *Topography influence on the lake equations in bounded domains.* Journal of Mathematical Fluid Mechanics **16** (2014), 375–406.
- **[SOTA]** J. Dekeyser, J. Van Schaftingen. *Vortex motion for the lake equations.* Communications in Mathematical Physics **375** (2020), 1459–1501.
- **[Technique]** E. Fabes, C. Kenig, R. Serapioni. *The local regularity of solutions of degenerate elliptic equations.* Communications in Partial Differential Equations **7** (1982), 77–116.
- **[Classical]** V. I. Yudovich. *Non-stationary flow of an ideal incompressible liquid.* Zhurnal Vychislitel'noi Matematiki i Matematicheskoi Fiziki **3** (1963), 1032–1066.
- **[Survey]** D. Bresch. *Shallow-water equations and related topics.* In: Handbook of Differential Equations: Evolutionary Equations, Vol. 5, Elsevier, 2009, 1–104.
- **[Related]** M. Oliver. *Justification of the shallow-water limit for a rigid-lid flow with bottom topography.* Theoretical and Computational Fluid Dynamics **9** (1997), 311–324.

## 10. Worked Example / Concrete Special Case

**A radially symmetric lake with a linear beach.** Take $\Omega = \{|x|<1\}$ and

$$b(r) = 1-r^2 \qquad (\text{so } b \simeq 2\,d \text{ near the shore, i.e. } a=1).$$

Take constant potential vorticity $q\equiv 1$. Radial symmetry gives $v = u_\theta(r)\,e_\theta$ and $v\cdot\nabla q = 0$, so this is a **stationary solution**. Solve the degenerate elliptic problem $\nabla\cdot(b^{-1}\nabla\psi)=bq$ in radial form:

$$\frac1r\left(\frac{r\,\psi'}{b}\right)' = b = 1-r^2 \;\Longrightarrow\; \frac{r\,\psi'}{b} = \int_0^r s(1-s^2)\,ds = \frac{r^2}{2}-\frac{r^4}{4}.$$

Hence

$$u_\theta(r) = \frac{\psi'(r)}{b(r)} = \frac{r}{2}-\frac{r^3}{4}, \qquad \psi'(r) = (1-r^2)\left(\frac r2 - \frac{r^3}{4}\right).$$

Check: $\omega = \frac1r (r u_\theta)' = \frac1r\bigl(\tfrac{r^2}{2}-\tfrac{r^4}{4}\bigr)' = 1-r^2 = b$, so $q=\omega/b=1$ ✓.

Two features are the whole story of the problem:

1. **The cancellation is real but delicate.** At the shore $b(1)=0$, yet $u_\theta(1)=\tfrac14$ is finite and smooth, because $\nabla\psi$ vanishes at exactly the same linear rate as $b$. Energy $E=\tfrac12\int_0^1 (1-r^2)u_\theta^2\,2\pi r\,dr = \tfrac{\pi}{2}\int_0^1 (1-r^2)\bigl(\tfrac r2-\tfrac{r^3}{4}\bigr)^2 2r\,dr$ is finite and explicitly computable ($=\tfrac{11\pi}{1120}$ after expanding the polynomial). No singularity forms.
2. **Symmetry, not general theory, produced the cancellation.** Replace $b=1-r^2$ by $b=(1-r^2)^a$: the same computation gives $u_\theta(r)=\frac{1-(1-r^2)^{a+1}}{2(a+1)r}$, bounded for every $a>0$. But the weight $b^{-1}\simeq d^{-a}$ lies in the Muckenhoupt class $A_2$ **only for $a<1$**. For $a\ge 1$ no off-the-shelf degenerate-elliptic estimate certifies that the same cancellation survives for *non-radial* $q_0 \in L^\infty$ — that is precisely the content of the Bresch–Métivier theorem, and precisely what remains unavailable when $b$ vanishes at an interior point or is merely bounded measurable.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*