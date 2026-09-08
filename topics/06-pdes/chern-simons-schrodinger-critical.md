---
id: 06-pdes/chern-simons-schrodinger-critical
title: "Global Well-posedness of the Chern-Simons-Schrodinger Equation at Critical Regularity"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Well-posedness of the Chern-Simons-Schrödinger Equation at Critical Regularity

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/chern-simons-schrodinger-critical` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Chern–Simons–Schrödinger (CSS) system is the planar gauged nonlinear Schrödinger equation of Jackiw–Pi. It is $L^2$-critical: the scaling $u\mapsto \lambda u(\lambda^2 t,\lambda x)$ leaves the mass $\|u\|_{L^2}$ invariant. The problem has three linked parts.

**(A) Critical-regularity local theory.** Is CSS locally well-posed in the scaling-critical space $L^2(\mathbb{R}^2)$ (in a suitable gauge, with continuous data-to-solution map on bounded sets)? No local theory below $H^1$ is known without equivariance.

**(B) Threshold conjecture (self-dual case $g=1$).** For equivariant data of index $m$, every $u_0\in L^2_m$ with
$$\|u_0\|_{L^2}^2 < \|Q^{(m)}\|_{L^2}^2 = 8\pi(m+1)$$
generates a unique global solution which scatters as $t\to\pm\infty$. Global existence is known in $H^1_m$; the statement at critical regularity $L^2_m$, and scattering in any regularity, are open.

**(C) The non-equivariant threshold.** Without symmetry, is there a mass threshold below which all $L^2$ solutions are global and scattering, and is that threshold $\|Q^{(0)}\|_{L^2}^2=8\pi$?

A complete resolution requires either a proof of (A)–(C) or a counterexample: an $L^2$ data set below threshold whose solution fails to exist globally, or a demonstration that the flow map is discontinuous on $L^2$.

## 2. Mathematical Foundations

Fields are $\phi:\mathbb{R}^{1+2}\to\mathbb{C}$ and a connection $A_\mu:\mathbb{R}^{1+2}\to\mathbb{R}$, $\mu=0,1,2$. Set
$$D_\mu = \partial_\mu - iA_\mu,\qquad F_{\mu\nu}=\partial_\mu A_\nu - \partial_\nu A_\mu .$$
The Euler–Lagrange equations of the Chern–Simons–Schrödinger Lagrangian are
$$D_t\phi = i\,D_\ell D_\ell \phi + i\,g\,|\phi|^2\phi,$$
$$F_{01} = -\operatorname{Im}(\bar\phi\, D_2\phi),\qquad F_{02} = \operatorname{Im}(\bar\phi\, D_1\phi),\qquad F_{12} = -\tfrac12|\phi|^2 .$$
The last three are elliptic/transport constraints, not evolution equations: $A$ is determined nonlocally by $\phi$. The system is invariant under $\phi\mapsto e^{i\chi}\phi$, $A_\mu\mapsto A_\mu+\partial_\mu\chi$, so a gauge (Coulomb $\partial_\ell A_\ell=0$, or the heat gauge of Liu–Smith–Tataru) must be fixed.

Conserved quantities: mass $M(\phi)=\int|\phi|^2$ and energy
$$E(\phi)=\int_{\mathbb{R}^2}\Big(|D\phi|^2-\tfrac{g}{2}|\phi|^4\Big)\,dx .$$
In the **self-dual case $g=1$** the Bogomolny factorization holds,
$$E(\phi)=\int_{\mathbb{R}^2}\big|(D_1+iD_2)\phi\big|^2\,dx \;\ge\; 0 .$$

**Equivariant reduction.** For $\phi(t,x)=e^{im\theta}u(t,r)$, $m\in\mathbb{Z}_{\ge0}$, with $A_r=0$, the system collapses to a scalar nonlocal equation
$$i\partial_t u + \Delta_m u = \Big(\frac{2mA_\theta+A_\theta^2}{r^2}-A_0\Big)u - |u|^2u,\qquad \Delta_m=\partial_r^2+\tfrac1r\partial_r-\tfrac{m^2}{r^2},$$
$$A_\theta(t,r)=-\tfrac12\int_0^r |u|^2 r'\,dr',\qquad A_0(t,r)=-\int_r^\infty (m+A_\theta)\,|u|^2\,\frac{dr'}{r'} .$$
Scaling $u_\lambda(t,r)=\lambda u(\lambda^2t,\lambda r)$ is an exact symmetry, so $L^2$ is critical; the system also enjoys the pseudoconformal symmetry of mass-critical NLS.

**Ground state.** The static self-dual solution solving the Bogomolny equation $\partial_r Q=\frac{m+A_\theta}{r}Q$ is explicit:
$$Q^{(m)}(r)=\sqrt{8}\,(m+1)\,\frac{r^m}{1+r^{2m+2}},\qquad \|Q^{(m)}\|_{L^2}^2=8\pi(m+1),\qquad E(Q^{(m)})=0 .$$

## 3. History & State of the Art (SOTA)

- **1990.** Jackiw and Pi introduce nonrelativistic Chern–Simons matter theory and find the self-dual solitons $Q^{(m)}$ (PRL 64, Phys. Rev. D 42). The model describes anyonic quantum Hall physics.
- **1995.** Bergé, de Bouard and Saut give the first rigorous PDE analysis: local existence in weighted $H^1$ and virial-type finite-time blow-up for $g>1$.
- **2009–2013.** Huh constructs explicit pseudoconformal blow-up by applying the pseudoconformal transform to $Q^{(m)}$, and proves existence (without uniqueness) of energy-space solutions.
- **2014.** Liu, Smith and Tataru prove local well-posedness in $H^s$, $s\ge1$, in a heat gauge, with continuation criteria and small-data global bounds. This remains the best non-equivariant local theory.
- **2015.** Oh and Pusateri prove global existence and modified/linear scattering for small, smooth, spatially localized data (non-self-dual coupling included).
- **2016.** Liu and Smith prove global well-posedness in the equivariant energy space $H^1_m$ for $g=1$ below the ground-state mass, and for all data when $g<1$.
- **2019–2023.** Kim and Kwon (Memoirs AMS 284, 2023) classify pseudoconformal blow-up at exactly threshold mass and prove it is *unstable*, unlike mass-critical NLS. Kim, Kwon and Oh construct and classify blow-up for $m\ge1$ above the threshold and prove soliton resolution in a weighted equivariant class.

The state of the art is therefore: sharp blow-up dynamics for $m\ge1$ in high regularity, but **no critical $L^2$ theory in any setting** and **no scattering statement below threshold**.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| Non-equivariant, $H^s$, $s\ge1$ | Local well-posedness, heat gauge | Liu–Smith–Tataru 2014 |
| Non-equivariant, small data in $H^{s}\cap$ weighted spaces | Global existence + decay $\|u\|_{L^\infty}\lesssim t^{-1}$, scattering | Oh–Pusateri 2015 |
| Equivariant $m\ge1$, $g=1$, $u_0\in H^1_m$, $\|u_0\|_{L^2}<\|Q^{(m)}\|_{L^2}$ | Global well-posedness | Liu–Smith 2016 |
| Equivariant, $g<1$ (subcritical coupling), $H^1_m$ | Global well-posedness, all data | Liu–Smith 2016 |
| $g>1$, weighted $H^1$, negative energy | Finite-time blow-up (virial) | Bergé–de Bouard–Saut 1995 |
| $g=1$, $m\ge1$, mass $=\|Q^{(m)}\|_{L^2}$ | Pseudoconformal blow-up $\lambda(t)\sim|t|$; uniqueness within the class; instability | Kim–Kwon 2023 |
| $g=1$, $m\ge1$, smooth data slightly above threshold | Blow-up with rate $\lambda(t)\sim t\,e^{-\sqrt{2|\log t|}}$ for $m=1$; codimension description for $m\ge1$ | Kim–Kwon–Oh 2020 |
| $g=1$, $m\ge1$, weighted Sobolev | Soliton resolution: modulated $Q^{(m)}$ + radiation | Kim–Kwon–Oh 2022 |

The threshold $8\pi(m+1)$ is therefore **sharp at the $H^1$ level** for $m\ge1$: below it solutions are global, at it blow-up exists.

## 5. Principal Obstacles

- **Derivative nonlinearity with nonlocal coefficients.** After gauge fixing, the equation contains $A_\ell\partial_\ell u$ with $A_\ell\sim \Delta^{-1}\nabla(|u|^2)$. This is a quadratic derivative term of exactly critical scaling: standard Strichartz iteration loses one derivative and Kato smoothing recovers only half in 2D. No contraction has been produced in any $L^2$-based critical space.
- **Loss of uniform continuity.** The gauge-covariant structure forces the use of $U$-$V$-type or heat-gauge function spaces where the nonlinear estimates are not perturbative; the data-to-solution map is not known to be uniformly continuous below $H^1$, which rules out the usual limiting arguments.
- **Nonnegative self-dual energy defeats virial.** Since $E\ge0$ when $g=1$, the Glassey identity $\partial_t^2\int|x|^2|u|^2=16E\ge0$ gives *no* blow-up criterion and no coercivity beyond the trivial one; concentration–compactness must therefore be run against a threshold detected only by mass, with $E=0$ at the threshold object.
- **Degenerate spectral structure of $Q^{(m)}$.** The linearized operator around $Q^{(m)}$ has a nonstandard, non-self-adjoint form with a "rotational" instability direction absent for NLS. Standard modulation with the NLS-type generalized null space fails; Kim–Kwon needed a bespoke conjugation (a Bogomolny-adapted factorization) to invert it.
- **Slow decay at $m=0$.** $Q^{(0)}(r)\sim 2\sqrt2\,r^{-2}$, so $Q^{(0)}\notin \Sigma$-type weighted classes needed for pseudoconformal arguments, and the linearized operator has a zero-energy resonance. All refined blow-up analysis is restricted to $m\ge1$.
- **Non-equivariant gauge geometry.** Without symmetry the connection cannot be solved for by a one-dimensional integral; the elliptic constraints produce genuinely two-dimensional nonlocal operators with no known critical-space multiplier bounds.

## 6. The Gap

Proven: $H^1_m$ global existence below threshold ($m\ge1$), plus a complete blow-up picture above it in high-regularity weighted classes. Conjectured: the same dichotomy in $L^2$, with scattering.

The exact missing steps are:
1. **A critical local theory.** Construct a function space $X\hookrightarrow C_tL^2_x$ in which the term $\frac{2mA_\theta+A_\theta^2}{r^2}u - A_0u$ is estimated perturbatively for arbitrary (not small) $L^2$ data over short times. Even for equivariant data this is unavailable — the $r^{-2}A_\theta$ term is scaling-critical and not controlled by any known Strichartz/local-smoothing pairing.
2. **A rigidity theorem.** Rule out the minimal-mass "almost-periodic" critical element produced by profile decomposition. For NLS this uses the virial/Morawetz identity; here $E\ge0$ makes the identity vacuous, so a new monotonicity formula adapted to the Bogomolny operator $\mathbf{D}=D_1+iD_2$ is needed.
3. **The $m=0$ and non-equivariant cases**, where even the $H^1$ threshold statement is not established.

## 7. Current Research (as of June 2026)

- **KAIST / Berkeley / IHES axis (Kwon, Kim, Oh).** The dominant program: modulation analysis in the "Bogomolny-conjugated" variables, giving soliton resolution and blow-up classification. Extension of resolution from weighted Sobolev to the energy space, and then to $L^2$, is the announced next step *(frontier — verify)*.
- **Critical function spaces.** Adaptation of Tataru-style heat-gauge $U^2/V^2$ spaces to reach $H^s$, $s<1$, non-equivariantly; partial progress reported for $s>1/2$ *(frontier — verify)*.
- **Continuity of the flow map.** Attempts to prove the $L^2$ flow map is *not* uniformly continuous, which would show the problem is ill-posed in the Hadamard sense and reframe (A) as a question about weak solutions *(frontier — verify)*.
- **Numerics.** Spectral simulation of equivariant CSS near threshold to test whether the $m=1$ rate $\lambda(t)\sim te^{-\sqrt{2|\log t|}}$ is generic and whether $m=0$ blow-up occurs at all.
- **Related models.** Techniques are being cross-applied to the self-dual Maxwell–Chern–Simons–Schrödinger system and to equivariant harmonic map heat flow / Schrödinger maps, which share the $r^{-2}$ potential structure.

## 8. Future Work

- Build a critical Besov/atomic space in which the equivariant nonlocal potential is handled by a **null-structure** argument: $A_0$ and $A_\theta$ are both nonresonant against the covariant derivative, and exploiting this cancellation is the most-cited route (Liu–Smith–Tataru).
- Develop a **Bogomolny virial identity**: a monotone quantity built from $\mathbf{D}\phi$ rather than $\nabla\phi$, which would restore rigidity despite $E\ge0$.
- Settle the $m=0$ case by resolving the zero-energy resonance of the linearized operator, possibly via a logarithmically corrected modulation ansatz.
- Prove **scattering below threshold** in $H^1_m$ first; this is strictly easier than the $L^2$ statement and is widely regarded as the next obtainable theorem.
- Determine whether the non-equivariant threshold is $8\pi$ or strictly smaller, by testing whether non-symmetric minimizers exist.

## 9. Key References

- **[Foundational]** R. Jackiw, S.-Y. Pi. *Soliton solutions to the gauged nonlinear Schrödinger equation on the plane.* Physical Review Letters 64 (1990), 2969–2972.
- **[Foundational]** R. Jackiw, S.-Y. Pi. *Classical and quantal nonrelativistic Chern–Simons theory.* Physical Review D 42 (1990), 3500–3513.
- **[Foundational]** L. Bergé, A. de Bouard, J.-C. Saut. *Blowing up time-dependent solutions of the planar, Chern–Simons gauged nonlinear Schrödinger equation.* Nonlinearity 8 (1995), 235–253.
- **[Foundational]** H. Huh. *Blow-up solutions of the Chern–Simons–Schrödinger equations.* Nonlinearity 22 (2009), 967–974.
- **[SOTA]** B. Liu, P. Smith, D. Tataru. *Local wellposedness of Chern–Simons–Schrödinger.* International Mathematics Research Notices 2014, no. 23, 6341–6398.
- **[SOTA]** B. Liu, P. Smith. *Global wellposedness of the equivariant Chern–Simons–Schrödinger equation.* Revista Matemática Iberoamericana 32 (2016), no. 3, 751–794.
- **[SOTA]** S.-J. Oh, F. Pusateri. *Decay and scattering for the Chern–Simons–Schrödinger equations.* International Mathematics Research Notices 2015, no. 24, 13122–13147.
- **[SOTA / Recent]** K. Kim, S. Kwon. *On pseudoconformal blow-up solutions to the self-dual Chern–Simons–Schrödinger equation: existence, uniqueness, and instability.* Memoirs of the American Mathematical Society 284 (2023), no. 1409.
- **[SOTA / Recent]** K. Kim, S. Kwon, S.-J. Oh. *Blow-up dynamics for smooth finite energy radial data solutions to the self-dual Chern–Simons–Schrödinger equation.* arXiv:2010.03252 (2020).
- **[SOTA / Recent]** K. Kim, S. Kwon, S.-J. Oh. *Soliton resolution for equivariant self-dual Chern–Simons–Schrödinger equation in weighted Sobolev class.* arXiv:2202.07314 (2022).
- **[Background]** H. Huh, J. Seok. *The equivalence of the Chern–Simons–Schrödinger equations and its self-dual system.* Journal of Mathematical Physics 52 (2011), 052301.
- **[Survey]** P. Raphaël. *Stability and blow up for the nonlinear Schrödinger equation.* Clay Mathematics Institute lecture notes (Park City / IAS), 2008.
- **[Survey / comparison]** F. Merle, P. Raphaël. *The blow-up dynamic and upper bound on the blow-up rate for critical nonlinear Schrödinger equation.* Annals of Mathematics 161 (2005), 157–222.

## 10. Worked Example / Concrete Special Case

**Verify that $Q^{(0)}$ is a static zero-energy solution, and read off the threshold.**

Take $m=0$, $g=1$, $u(t,r)=Q(r)=\dfrac{2\sqrt2}{1+r^2}$.

*Step 1 — the connection.* From the constraint,
$$A_\theta(r)=-\tfrac12\int_0^r Q^2\,r'\,dr' = -\tfrac12\cdot 8\int_0^r \frac{r'\,dr'}{(1+r'^2)^2} = -4\cdot\frac{r^2}{2(1+r^2)} = -\frac{2r^2}{1+r^2}.$$

*Step 2 — the Bogomolny equation.* For equivariance $m$, $(D_1+iD_2)\phi=0$ reduces to $\partial_r Q=\frac{m+A_\theta}{r}Q$. With $m=0$:
$$\text{LHS}=\partial_r\frac{2\sqrt2}{1+r^2}=-\frac{4\sqrt2\,r}{(1+r^2)^2},\qquad \text{RHS}=\frac{1}{r}\Big(-\frac{2r^2}{1+r^2}\Big)\frac{2\sqrt2}{1+r^2}=-\frac{4\sqrt2\,r}{(1+r^2)^2}.$$
They agree identically. Hence $\mathbf{D}Q=0$ and, by the self-dual factorization, $E(Q)=\int|\mathbf{D}Q|^2=0$.

*Step 3 — the mass.*
$$\|Q\|_{L^2}^2=2\pi\int_0^\infty \frac{8}{(1+r^2)^2}\,r\,dr = 16\pi\cdot\frac12 = 8\pi = 8\pi(m+1).$$

*Step 4 — what this shows.* $Q$ is a stationary solution sitting exactly at the conjectured threshold with zero energy. Applying the pseudoconformal transform
$$u(t,r)=\frac{1}{|t|}\,e^{i\frac{r^2}{4t}-\frac{i}{t}}\,Q\!\Big(\frac{r}{|t|}\Big)$$
produces a solution with the same mass $8\pi$ that blows up as $t\to0^-$ with $\|\nabla u(t)\|_{L^2}\sim|t|^{-1}$ (rigorously constructed and classified for $m\ge1$ by Kim–Kwon). So no theorem can assert global existence at mass $\ge 8\pi(m+1)$, and the conjecture in Section 1 is sharp.

*Step 5 — where the critical theory breaks.* Perturb by $u_0=Q_\varepsilon$ with $\|Q_\varepsilon\|_{L^2}^2=8\pi-\varepsilon$. In $H^1$, Liu–Smith give a global solution. In $L^2$ the same data is admissible, but the term $\frac{A_\theta^2}{r^2}u$ scales exactly like $u$ in $L^2$ — with $A_\theta\sim -2$ for large $r$, it behaves as a critical inverse-square potential $-4r^{-2}u$, for which no $L^2$ perturbative estimate exists. That single term is the obstruction separating Section 4 from Section 1.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*