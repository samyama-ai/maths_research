---
id: 06-pdes/maxwell-klein-gordon-regularity
title: "Maxwell Klein Gordon Regularity"
topic: 06-pdes
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Global Regularity for the Maxwell–Klein–Gordon Equations

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/maxwell-klein-gordon-regularity` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

The Maxwell–Klein–Gordon (MKG) system is the gauge-covariant coupling of a complex scalar field to an electromagnetic potential — the Euler–Lagrange system of the simplest non-abelian-adjacent gauge theory, and the standard scalar model problem for Yang–Mills.

**Threshold Conjecture (MKG).** Every smooth, finite-energy initial data set for the massless MKG system on Minkowski space $\mathbb{R}^{1+4}$ launches a unique global smooth solution that scatters to a free solution as $t \to \pm\infty$, with no energy threshold.

Dimension $4+1$ is singled out because it is *energy critical*: the scaling that preserves the equation also preserves the conserved energy, so no smallness assumption is available from conservation laws alone. A complete proof must (i) construct a global solution for arbitrarily large finite-energy data, (ii) propagate all higher Sobolev regularity, and (iii) establish scattering. A disproof would exhibit finite-energy data whose maximal solution has a finite lifespan — necessarily by concentration of energy at a point of the light cone.

**Status.** The conjecture is a theorem, proved in the massless case by Sung-Jin Oh and Daniel Tataru (2016–2018) and, in the equivariant class, independently by Joachim Krieger and Jonas Lührmann. What remains open is stated in Sections 5–6: the energy-supercritical regime $d \ge 5$ at large data, the massive $4+1$ problem, and sharp critical-regularity local theory in $3+1$.

## 2. Mathematical Foundations

Let $\mathbb{R}^{1+d}$ carry the Minkowski metric $m = \mathrm{diag}(-1,1,\dots,1)$. The unknowns are a connection one-form $A = A_\alpha\,dx^\alpha$ (real-valued) and a section $\phi:\mathbb{R}^{1+d}\to\mathbb{C}$ of the associated line bundle. Define the covariant derivative and curvature

$$D_\alpha \phi = (\partial_\alpha - i A_\alpha)\phi, \qquad F_{\alpha\beta} = \partial_\alpha A_\beta - \partial_\beta A_\alpha .$$

The MKG system is

$$\partial^\beta F_{\alpha\beta} = J_\alpha := \Im\big(\phi \,\overline{D_\alpha \phi}\big), \qquad D^\alpha D_\alpha \phi = m^2\phi ,$$

with $m = 0$ in the massless case. It is the critical point of the action $\mathcal{L}[A,\phi] = \int \tfrac14 F_{\alpha\beta}F^{\alpha\beta} + \tfrac12 D_\alpha\phi\,\overline{D^\alpha\phi} + \tfrac{m^2}{2}|\phi|^2$.

**Gauge invariance.** For any $\chi:\mathbb{R}^{1+d}\to\mathbb{R}$, the map $(A,\phi)\mapsto (A + d\chi,\ e^{i\chi}\phi)$ preserves solutions. The system is therefore not hyperbolic as written and a gauge must be imposed. The two standard choices:

- **Coulomb gauge** $\partial^j A_j = 0$. Then $A_0$ is determined *elliptically*, $\Delta A_0 = -\Im(\bar\phi D_0\phi)$, while the dynamical components satisfy
$$\Box A_j = -\mathcal{P}_j\,\Im(\bar\phi\, D\phi), \qquad \Box_A \phi := D^\alpha D_\alpha\phi = m^2\phi,$$
with $\mathcal{P}$ the Leray projection onto divergence-free fields.
- **Lorenz gauge** $\partial^\alpha A_\alpha = 0$, giving $\Box A_\alpha = J_\alpha$, manifestly covariant but with weaker null structure.

**Conserved energy.** On $\{t = \text{const}\}$,
$$E[A,\phi] = \int_{\mathbb{R}^d}\Big(\tfrac12\textstyle\sum_i |F_{0i}|^2 + \tfrac14\sum_{i,j}|F_{ij}|^2 + \tfrac12\sum_\alpha |D_\alpha\phi|^2 + \tfrac{m^2}{2}|\phi|^2\Big)\,dx .$$

**Scaling.** With $m=0$, if $(A,\phi)$ solves MKG so does
$$(A_\lambda,\phi_\lambda)(t,x) = \big(\lambda A(\lambda t,\lambda x),\ \lambda \phi(\lambda t,\lambda x)\big),$$
which is invariant in $\dot H^{s_c}\times \dot H^{s_c-1}$ with $s_c = \tfrac d2 - 1$. Hence $s_c = 1$ in $d=4$ (energy critical), $s_c = 1/2$ in $d = 3$ (energy subcritical), $s_c > 1$ for $d \ge 5$ (energy supercritical).

**Constraint.** Data must satisfy the Gauss law $\partial^j F_{0j} = \Im(\phi\overline{D_0\phi})$ at $t=0$; it is propagated by the flow.

**Null structure.** The dangerous quadratic term in the Coulomb gauge is $2iA^j\partial_j\phi$. Because $A^j$ is divergence-free, this is not a generic bilinear form: schematically it reduces to the null forms
$$Q_{ij}(u,v) = \partial_i u\,\partial_j v - \partial_j u\,\partial_i v,$$
whose symbol vanishes on parallel null frequencies. This cancellation, discovered by Klainerman–Machedon, is the structural fact on which all sharp results rest.

## 3. History & State of the Art (SOTA)

- **1982.** Eardley and Moncrief prove global existence of smooth solutions to the Yang–Mills–Higgs equations (which contain MKG) in $\mathbb{R}^{1+3}$ for smooth data, using a parametrix and the null structure implicitly.
- **1994.** Klainerman and Machedon give a genuinely low-regularity proof: finite-energy ($H^1\times L^2$) global well-posedness in $3+1$ in the Coulomb gauge, by isolating the null forms $Q_{ij}$ and proving bilinear estimates in $X^{s,b}$ spaces.
- **1999–2004.** Cuccagna, then Machedon and Sterbenz, push local well-posedness in $3+1$ down to $s > 1/2 + \varepsilon$ and then to almost the scaling exponent $s_c = 1/2$; Keel–Roy–Tao obtain global well-posedness below the energy norm for $s > \sqrt3/2$.
- **2004.** Rodnianski and Tao prove global regularity in high dimensions $d \ge 6$ for data small in the critical Sobolev norm $\dot H^{s_c}$, introducing microlocal gauge renormalization (a pseudodifferential parametrix conjugating away the magnetic potential).
- **2015.** Krieger, Sterbenz and Tataru settle the **small-energy** energy-critical case $d = 4$.
- **2015–2018.** Krieger–Lührmann develop concentration-compactness for critical MKG and resolve the equivariant large-energy case. Oh–Tataru complete the general large-energy $4+1$ threshold theorem in a three-paper program.
- **2019–2021.** Yang and Yu establish global existence and sharp pointwise decay for the *massive* MKG system in $3+1$ with small data; Oh–Tataru transfer the method to prove the threshold theorem for the $4+1$ Yang–Mills equation.

## 4. Partial Results / Verified Cases

| Regime | Result | Reference |
|---|---|---|
| $d=3$, $s \ge 1$ (finite energy) | Global regularity, Coulomb gauge | Klainerman–Machedon 1994 |
| $d=3$, $s > 1/2$ | Local well-posedness, almost critical | Machedon–Sterbenz 2004 |
| $d=3$, $s > \sqrt3/2$ | Global well-posedness below energy | Keel–Roy–Tao 2011 |
| $d=3$, Lorenz gauge, finite energy | Global well-posedness | Selberg–Tesfahun 2010 |
| $d \ge 6$, small $\dot H^{s_c}$ | Global regularity + scattering | Rodnianski–Tao 2004 |
| $d = 4$, small energy | Global well-posedness + scattering | Krieger–Sterbenz–Tataru 2015 |
| $d = 4$, equivariant, arbitrary energy | Global regularity | Krieger–Lührmann 2015 |
| $d = 4$, arbitrary energy, $m = 0$ | **Global well-posedness + scattering** | Oh–Tataru 2016–2018 |
| $d = 3$, massive, small data | Global existence, pointwise decay $t^{-3/2}$ for $\phi$ | Yang–Yu 2019 |

The energy-critical case is therefore fully resolved in the massless setting; the $3+1$ case is resolved above scaling but not at it; $d\ge5$ is resolved only under a critical-norm smallness assumption.

## 5. Principal Obstacles

- **Gauge invariance destroys hyperbolicity.** No single gauge is simultaneously local, hyperbolic, and well-behaved at critical regularity. Coulomb gauge is elliptic-hyperbolic and non-local, so finite speed of propagation and the induction-on-energy machinery of critical NLS/wave must be rebuilt by hand; Lorenz gauge is local but the null structure is weaker.
- **Loss of derivatives in the magnetic interaction.** The term $A^j\partial_j\phi$ has the same number of derivatives as the free wave operator. At critical regularity $A^j$ is only $\dot H^1$-bounded in $d=4$, so no perturbative iteration in Strichartz or $X^{s,b}$ spaces closes; $A$ must be *renormalized* into the operator via a pseudodifferential conjugation $e^{-i\psi(x,D)}$, and the error terms must be controlled in a functional framework ($S^1$, $N$, null-frame $\mathrm{NE}$ spaces) built for that purpose.
- **Failure of standard concentration compactness.** Bahouri–Gérard/Kenig–Merle profile decomposition requires a bounded-energy sequence of solutions with a well-defined free evolution. The Coulomb gauge condition is not preserved under the translations and Lorentz boosts that generate profiles, and the elliptic component $A_0$ is not a profile of the linear flow. Krieger–Lührmann and Oh–Tataru have to prove a *gauge-covariant* profile decomposition.
- **No monotonicity.** MKG has no known Morawetz or virial identity strong enough to rule out self-similar or soliton-like concentration directly. The exclusion of a minimal-energy blowup solution proceeds instead through an energy-dispersion criterion: solutions whose $L^\infty_{t,x}$-type dispersive norm is small are global, so blowup forces a nontrivial concentration bubble, which is then removed by the classification of finite-energy solutions of the elliptic/self-similar limit.
- **Supercriticality above $d=4$.** For $d\ge5$ conservation of energy controls a strictly weaker norm than scaling, and there is no substitute conserved quantity. Every current method requires an *a priori* critical-norm bound, which is exactly what is missing.

## 6. The Gap

The gap has moved rather than closed. Three specific boundaries remain:

1. **Massless $d=4$ → massive $d=4$.** The mass term $m^2\phi$ breaks scale invariance and changes the low-frequency behaviour of the scalar; the null-frame spaces used by Oh–Tataru are tuned to the massless dispersion relation $|\tau|=|\xi|$. Extending the threshold theorem, including scattering to a free *massive* Klein–Gordon evolution, is open. *(frontier — verify)*
2. **$d \ge 5$ small critical norm → large data.** Even in $d = 5$ the only route would be an a priori bound on $\|\phi\|_{\dot H^{3/2}}$; nothing in the structure supplies it. This is the exact analogue of the supercritical wave-equation problem and is expected to be very hard.
3. **$d=3$ at $s = s_c = 1/2$.** Local well-posedness is known for $s>1/2$; the endpoint $s=1/2$, where the null-form bilinear estimates fail logarithmically, remains open, as does global well-posedness at $s = 1/2$.

## 7. Current Research (as of June 2026)

- **Berkeley / KIAS (Oh, Tataru and collaborators).** Extension of the renormalization + energy-dispersion architecture to Yang–Mills in $4+1$ (completed) and, currently, to the massive MKG and Maxwell–Dirac systems, and to curved backgrounds. *(frontier — verify)*
- **EPFL (Krieger and students).** Concentration-compactness under symmetry, construction of *non-generic* blowup and threshold solutions for critical gauge models, in the spirit of the Krieger–Schlag–Tataru wave-map constructions. Whether MKG admits a critical-energy self-similar or type-II object outside the equivariant class is the natural test question. *(frontier — verify)*
- **Peking / Tsinghua (Yang, Yu and collaborators).** Vector-field and $r^p$-weighted methods for global dynamics and sharp decay of massive MKG in $3+1$, including large-data results with small Maxwell field.
- **Oslo / NTNU (Selberg, Tesfahun and collaborators).** Low-regularity and gauge-comparison results, in particular Lorenz-gauge local theory and Maxwell–Dirac.
- **Numerical / structural.** Equivariant simulations of critical MKG probing whether energy concentrates on a bubble of the static Yang–Mills instanton type; no counterexample to global regularity has been observed.

## 8. Future Work

- Transfer the massless $4+1$ threshold argument to the massive case by constructing null-frame spaces adapted to the hyperboloidal foliation used by Yang–Yu.
- Prove a conditional regularity criterion in $d\ge5$: global regularity assuming a priori boundedness of $\|\phi\|_{L^\infty_t \dot H^{s_c}}$, with a quantitative (non-compactness) proof yielding effective bounds.
- Settle the endpoint $s=1/2$ in $3+1$, possibly by adapted $U^p/V^p$ atomic spaces replacing $X^{s,b}$.
- Extend the threshold theorem to MKG on curved backgrounds (Schwarzschild, Kerr), where trapping obstructs the null-frame decomposition.
- Understand whether the Oh–Tataru machinery can be made to produce *quantitative* bounds on the higher Sobolev norms in terms of energy; the current argument is by contradiction and gives none.

## 9. Key References

- **[Foundational]** D. Eardley and V. Moncrief. *The global existence of Yang–Mills–Higgs fields in 4-dimensional Minkowski space, I & II.* Communications in Mathematical Physics 83 (1982), 171–191 and 193–212.
- **[Foundational]** S. Klainerman and M. Machedon. *On the Maxwell–Klein–Gordon equation with finite energy.* Duke Mathematical Journal 74 (1994), 19–44.
- **[Foundational]** M. Machedon and J. Sterbenz. *Almost optimal local well-posedness for the (3+1)-dimensional Maxwell–Klein–Gordon equations.* Journal of the American Mathematical Society 17 (2004), 297–359.
- **[Foundational]** I. Rodnianski and T. Tao. *Global regularity for the Maxwell–Klein–Gordon equation with small critical Sobolev norm in high dimensions.* Communications in Mathematical Physics 251 (2004), 377–426.
- **[SOTA / Recent]** J. Krieger, J. Sterbenz and D. Tataru. *Global well-posedness for the Maxwell–Klein–Gordon equation in 4+1 dimensions: small energy.* Duke Mathematical Journal 164 (2015), 973–1040.
- **[SOTA / Recent]** J. Krieger and J. Lührmann. *Concentration compactness for the critical Maxwell–Klein–Gordon equation.* Annals of PDE 1 (2015), Article 5.
- **[SOTA / Recent]** S.-J. Oh and D. Tataru. *Local well-posedness of the (4+1)-dimensional Maxwell–Klein–Gordon equation at energy regularity.* Annals of PDE 2 (2016), Article 2.
- **[SOTA / Recent]** S.-J. Oh and D. Tataru. *Energy dispersed solutions for the (4+1)-dimensional Maxwell–Klein–Gordon equation.* American Journal of Mathematics 140 (2018), 1–82.
- **[SOTA / Recent]** S.-J. Oh and D. Tataru. *Global well-posedness and scattering of the (4+1)-dimensional Maxwell–Klein–Gordon equation.* Inventiones Mathematicae 205 (2016), 781–877.
- **[SOTA / Recent]** S. Yang and P. Yu. *On global dynamics of the Maxwell–Klein–Gordon equations.* Cambridge Journal of Mathematics 7 (2019), 365–467.
- **[Recent]** M. Keel, T. Roy and T. Tao. *Global well-posedness of the Maxwell–Klein–Gordon equation below the energy norm.* Discrete and Continuous Dynamical Systems 30 (2011), 573–621.
- **[Recent]** S. Selberg and A. Tesfahun. *Finite-energy global well-posedness of the Maxwell–Klein–Gordon system in Lorenz gauge.* Communications in Partial Differential Equations 35 (2010), 1029–1057.
- **[Survey]** S.-J. Oh and D. Tataru. *The threshold theorem for the (4+1)-dimensional Yang–Mills equation: an overview of the proof.* Bulletin of the American Mathematical Society 56 (2019), 171–210.

## 10. Worked Example / Concrete Special Case

**Claim.** Verify that $d = 4$ is exactly the energy-critical dimension, and see where the perturbative argument breaks.

*Step 1 — scaling of the energy.* Take $m = 0$ and $(A_\lambda,\phi_\lambda)(t,x) = (\lambda A,\lambda\phi)(\lambda t,\lambda x)$. Then $F_{\alpha\beta}[A_\lambda] = \lambda^2 F_{\alpha\beta}[A](\lambda\cdot)$ and $D_\alpha\phi_\lambda = \lambda^2 (D_\alpha\phi)(\lambda\cdot)$. Substituting into the energy,
$$E[A_\lambda,\phi_\lambda] = \int_{\mathbb{R}^d} \lambda^4 \,\big(\text{energy density}\big)(\lambda x)\,dx = \lambda^{4-d}\,E[A,\phi].$$
So $E$ is scale invariant precisely when $d = 4$. For $d = 3$, $E[A_\lambda,\phi_\lambda] = \lambda\,E$: shrinking to small scales *costs* energy, which is why Klainerman–Machedon can close a global argument from energy conservation alone. For $d = 5$, $E$ scales like $\lambda^{-1}$: energy becomes free at small scales, and conservation gives nothing.

*Step 2 — the term that resists iteration.* In Coulomb gauge, expanding $D^\alpha D_\alpha\phi = 0$,
$$\Box \phi = 2i A^j \partial_j \phi + 2iA_0\partial_t\phi + i(\partial_t A_0)\phi + A^\alpha A_\alpha \phi .$$
Estimate the leading term perturbatively in $d = 4$. Energy data give $A \in L^\infty_t \dot H^1$ and $\nabla\phi \in L^\infty_t L^2$; Sobolev embedding in $\mathbb{R}^4$ gives $\dot H^1 \hookrightarrow L^4$, so
$$\|A^j\partial_j\phi\|_{L^\infty_t L^{4/3}_x} \lesssim \|A\|_{L^4}\|\nabla\phi\|_{L^2} \lesssim E .$$
The Duhamel/Strichartz step requires a bound in $L^1_t L^2_x$ (or the dual $N$-space), and $L^{4/3}_x$ is exactly one Sobolev derivative short of $L^2_x$ at this scaling. The deficit is scale-invariant: it does not improve on short time intervals, so no continuity/bootstrap argument recovers it. This is the "loss of a derivative" of Section 5.

*Step 3 — what the null structure buys.* Write $\hat A^j(\xi)$ divergence-free, i.e. $\xi_j \hat A^j = 0$. Then for a high-frequency $\phi$ of frequency $\eta$,
$$\big| \xi_j\ \text{-contraction} \big| : \quad \widehat{A^j\partial_j\phi} \ \sim \int \hat A^j(\xi)\,\eta_j\,\hat\phi(\eta)\,,\qquad \hat A^j(\xi)\xi_j = 0,$$
so $\hat A^j(\xi)\eta_j = \hat A^j(\xi)(\eta-\xi)_j$, and the symbol carries the factor $|\eta - \xi|\sin\angle(\xi,\eta)$ rather than $|\eta|$. When $\xi$ and $\eta$ are nearly parallel — the resonant configuration responsible for the failure above — the symbol vanishes to first order in the angle. This is the $Q_{ij}$ cancellation, and it is what converts the $L^{4/3}$ deficit into a usable estimate for *small* energy (Krieger–Sterbenz–Tataru). For large energy the gain is still insufficient at a single frequency interaction, and the potential must instead be removed by the renormalization $\phi \mapsto e^{-i\psi_{<k}(t,x,D)}\phi$ used by Rodnianski–Tao and Oh–Tataru, where $\psi_{<k}$ solves an approximate eikonal equation driven by the low-frequency part of $A$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*