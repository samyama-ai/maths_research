---
id: 06-pdes/nls-solitary-wave-stability
title: "NLS Solitary Wave Stability"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# NLS Solitary Wave Stability

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/nls-solitary-wave-stability` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Consider the focusing nonlinear Schrödinger equation (NLS) on $\mathbb{R}^d$,

$$i\partial_t u + \Delta u + |u|^{p-1}u = 0, \qquad u(0,\cdot)=u_0 \in H^1(\mathbb{R}^d),$$

which admits **solitary waves** $u(t,x)=e^{i\omega t}Q_\omega(x)$ with $Q_\omega>0$ the ground state of $-\Delta Q_\omega + \omega Q_\omega = Q_\omega^p$.

Two questions, of increasing strength:

1. **Orbital stability.** Is the group orbit $\{e^{i\gamma}Q_\omega(\cdot-y)\}$ Lyapunov-stable in $H^1$? *Answered*: yes iff $\partial_\omega \|Q_\omega\|_{L^2}^2>0$ (Vakhitov–Kolokolov), i.e. iff $1<p<1+\tfrac4d$.
2. **Asymptotic stability and soliton resolution (open).** Conjecture: for generic nonlinearities and generic $H^1$ data, every global solution decomposes as $t\to\infty$ into a finite superposition of modulated solitary waves plus a free radiation field,
$$u(t) = \sum_{j=1}^{N} e^{i(\gamma_j(t)+ v_j\cdot x)} Q_{\omega_j}\!\big(x - x_j(t)\big) + e^{it\Delta}u_+ + o_{H^1}(1).$$
A complete resolution requires: (i) proving the decomposition for non-integrable $p$ and $d$ without smallness or spectral-genericity hypotheses; (ii) handling the $L^2$-critical case $p=1+\frac4d$, where orbital stability fails and blow-up/soliton dichotomies must be classified; (iii) ruling out exotic behaviour (soliton-like solutions that never resolve, infinite-time growth of $N$).

## 2. Mathematical Foundations

**Conserved quantities.** Mass $M(u)=\int|u|^2$, energy $E(u)=\frac12\int|\nabla u|^2-\frac{1}{p+1}\int|u|^{p+1}$, momentum $P(u)=\mathrm{Im}\int\bar u\nabla u$. Symmetries: phase $U(1)$, translation, Galilean boost, scaling $u_\lambda(t,x)=\lambda^{2/(p-1)}u(\lambda^2t,\lambda x)$.

**Ground state.** $Q=Q_1$ is the unique (up to translation) positive $H^1$ solution of $-\Delta Q+Q=Q^p$, existence by Berestycki–Lions (1983), uniqueness by Kwong (1989) for $1<p<\frac{d+2}{d-2}$. Scaling gives $Q_\omega(x)=\omega^{1/(p-1)}Q(\sqrt\omega x)$, hence

$$M(Q_\omega)=\omega^{\frac{2}{p-1}-\frac d2}\|Q\|_{L^2}^2 .$$

**Action and the VK function.** With $S_\omega=E+\frac{\omega}{2}M$ and $d(\omega):=S_\omega(Q_\omega)$, one has $d'(\omega)=\frac12 M(Q_\omega)$, so the Vakhitov–Kolokolov slope condition is $d''(\omega)>0$.

**Linearization.** Writing $u=e^{i\omega t}(Q_\omega+w)$, $w=w_1+iw_2$, the linearized generator is $JL$ with $J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and
$$L_+ = -\Delta+\omega - pQ_\omega^{p-1},\qquad L_- = -\Delta+\omega - Q_\omega^{p-1}.$$
$L_-\ge0$ with kernel $\mathrm{span}\{Q_\omega\}$; $L_+$ has exactly one negative eigenvalue and $\ker L_+=\mathrm{span}\{\partial_{x_j}Q_\omega\}$ (Weinstein 1985). The generalized kernel of $JL$ is spanned by the symmetry modes; $\dim\ker_{\rm gen}=4$ generically, jumping to $6$ at the critical exponent.

**GSS theorem** (Grillakis–Shatah–Strauss 1987/1990): if $n(L)-p(d'')=0$ the wave is orbitally stable; if the count is odd, it is exponentially unstable. Here $n(L)=1$, so stability $\iff d''(\omega)>0$.

**Asymptotic stability framework.** One writes $u(t)=e^{i\gamma(t)}\big(Q_{\omega(t)}(\cdot-x(t))+\eta(t)\big)$ with orthogonality conditions killing the generalized kernel, and must prove $\eta\to0$ locally, driven by dispersive decay of $e^{itH}$, $H=-\Delta+V$, $V$ built from $Q^{p-1}$, plus **Fermi Golden Rule** damping of internal modes.

## 3. History & State of the Art (SOTA)

- **1972** — Zakharov–Shabat solve the 1D cubic NLS by inverse scattering; solitons are stable and multi-soliton resolution holds exactly.
- **1973** — Vakhitov–Kolokolov derive the slope criterion heuristically in nonlinear optics.
- **1982–83** — Cazenave–Lions prove orbital stability by concentration-compactness on the constrained minimization problem; Weinstein establishes the sharp Gagliardo–Nirenberg constant $\|u\|_{L^{2+4/d}}^{2+4/d}\le C\|\nabla u\|_2^{2}\|u\|_2^{4/d}$ with extremizer $Q$, giving the mass threshold $\|u_0\|_2<\|Q\|_2$ for global existence in the critical case.
- **1985–86** — Weinstein's modulation/spectral proof of orbital stability for $p<1+4/d$; instability for $p\ge1+4/d$.
- **1987/1990** — GSS abstract Hamiltonian stability theory.
- **1990–2001** — Asymptotic stability programme: Soffer–Weinstein (multichannel scattering, small solitons with a linear bound state), Buslaev–Perelman (1D, states near a soliton), Cuccagna (dimension $\ge3$, spectrally generic potentials).
- **2004–2006** — Merle–Raphaël classify the log-log blow-up regime for critical NLS with $\|Q\|_2<\|u_0\|_2<\|Q\|_2+\alpha^*$.
- **2008–2010** — Duyckaerts–Merle and Duyckaerts–Roudenko classify threshold-energy solutions ($E\cdot M = E(Q)M(Q)$), exhibiting the special solutions $Q^\pm$ converging exponentially to the soliton.
- **2017–present** — Virial/localized-energy methods (Kowalczyk–Martel–Muñoz) give asymptotic stability without spectral genericity in 1D settings; extended to 1D NLS with internal modes.

## 4. Partial Results / Verified Cases

| Regime | Result |
|---|---|
| $1<p<1+\frac4d$, all $d\ge1$ | Orbital stability of $Q_\omega$ (Cazenave–Lions 1982; Weinstein 1986). |
| $p>1+\frac4d$, $p<\frac{d+2}{d-2}$ | Orbital instability; $d''(\omega)<0$, one unstable eigenvalue (Grillakis–Shatah–Strauss). |
| $p=1+\frac4d$ exactly | Instability by blow-up (Weinstein 1983, Merle 1993): the minimal-mass blow-up solution is the pseudoconformal transform of $e^{it}Q$, unique up to symmetries. |
| $d=1$, $p=3$ | Integrable; complete soliton resolution for Schwartz data via inverse scattering / nonlinear steepest descent. |
| $d\ge3$, $p$ near cubic, spectrally generic $L_+$ | Asymptotic stability of small solitons for NLS with potential (Soffer–Weinstein 1990; Cuccagna 2001, CPAM 54, 1110–1145). |
| Critical NLS, $\|Q\|_2<\|u_0\|_2<\|Q\|_2+\alpha^*$, negative energy | Log-log rate $\|\nabla u(t)\|_2\sim\big(\frac{\log|\log(T-t)|}{T-t}\big)^{1/2}$ (Merle–Raphaël, *Invent. Math.* 156 (2004); *Ann. of Math.* 161 (2005)). |
| Threshold $E(u_0)M(u_0)=E(Q)M(Q)$, 3D cubic | Exactly three behaviours up to symmetry: soliton, $Q^+$ (blow-up), $Q^-$ (scattering) — Duyckaerts–Roudenko 2010. |
| 1D cubic–quintic NLS, small solitary waves | Asymptotic stability without spectral hypotheses (Martel, *Invent. Math.* 2022) — virial method. |
| Multi-solitons, distinct velocities | Asymptotic stability of well-separated $N$-soliton configurations under decay + genericity (Perelman 2004; Rodnianski–Schlag–Soffer preprint). |

## 5. Principal Obstacles

- **Zero modes and slow decay.** The linearized operator $JL$ is non-self-adjoint with a $4$-dimensional generalized kernel from symmetries. Modulation removes it, but only at the price of coupled ODEs for $(\omega,\gamma,x,v)$ whose error terms are only $O(\|\eta\|^2)$ — not integrable in $t$ in low dimensions where $\|e^{it\Delta}\|_{L^1\to L^\infty}\sim t^{-d/2}$ decays too slowly for $d=1,2$.
- **Internal modes.** When $L$ has eigenvalues in $(0,\omega)$, the linear flow does not disperse. Damping requires a **Fermi Golden Rule** non-degeneracy: a resonance integral $\Gamma=\lim_{\varepsilon\to0}\mathrm{Im}\langle (H-2\lambda-i\varepsilon)^{-1}F,F\rangle>0$. Verifying $\Gamma\ne0$ for a *given* $(d,p)$ is an unresolved analytic/numerical problem — it is an implicit spectral condition, not a checkable inequality.
- **Threshold resonances.** Genericity of the zero-energy spectral point (no threshold resonance for $H$) is assumed in nearly all $d\ge3$ proofs; no method exists to verify or remove it for the *actual* soliton potential $-pQ^{p-1}$.
- **Critical exponent degeneracy.** At $p=1+4/d$, $d''(\omega)=0$ and GSS is silent. Comech–Pelinovsky (*CPAM* 56 (2003)) showed instability is *purely nonlinear*, driven by higher-order terms in the modulation expansion — no linear eigenvalue signals it.
- **Global-in-time control.** Soliton resolution needs a global compactness/rigidity argument (concentration-compactness + Kenig–Merle rigidity). Rigidity uses monotonicity of a virial or Morawetz functional; for NLS these functionals are not monotone in the presence of multiple moving solitons with near-equal speeds.

## 6. The Gap

Proven: orbital (in)stability is *completely settled* by the sign of $d''(\omega)$. Asymptotic stability is proven only under three hypotheses that are always assumed and never verified: (a) smallness of the soliton or of the perturbation in a weighted space $\langle x\rangle^{-\sigma}L^2$; (b) spectral genericity of $H$ (no threshold resonance, no eigenvalue at the edge); (c) a Fermi Golden Rule inequality on internal modes.

The exact step to be crossed: **remove (b) and (c) for the physical operators $L_\pm$ built from $Q$ itself**, and replace the weighted-space smallness in (a) by pure $H^1$ (or $L^2$) hypotheses. Equivalently, one needs a *structural* mechanism — a virial-type monotonicity adapted to the soliton — that produces local decay of $\eta$ without knowing the fine spectrum of $H$. Kowalczyk–Martel–Muñoz's method does this in 1D scalar field models; extending it to $\mathbb{R}^d$, $d\ge2$, with the full $U(1)\times$translation symmetry group, is the open frontier.

## 7. Current Research (as of June 2026)

- **Virial/localized-energy school** (Martel, Muñoz, Kowalczyk, and collaborators, Paris-Saclay / Pontificia Universidad Católica de Chile): pushing transformed-problem virial estimates to 1D NLS with internal modes and to non-generic potentials. Martel's cubic–quintic result is the template.
- **Space-time resonances / normal forms** (Germain, Collot, Ifrim, Tataru; Courant, ENS, Berkeley): treating 1D NLS asymptotic stability as a long-range modified-scattering problem. *(frontier — verify)* preprints of Collot–Germain claim asymptotic stability for 1D NLS solitary waves under generic spectral assumptions with pure $L^2$-type control.
- **Soliton resolution via channels of energy** (Duyckaerts, Kenig, Merle, Martel): fully proven for energy-critical wave equations in odd dimensions; the NLS analogue remains open because NLS lacks a finite speed of propagation and hence exterior-energy lower bounds.
- **Supercritical dynamics** (Merle–Raphaël–Rodnianski–Szeftel, *Invent. Math.* 227 (2022)): self-similar blow-up for energy-supercritical *defocusing* NLS, reshaping expectations about what "generic" behaviour means above the critical exponent.
- **Numerics/computer-assisted proofs**: rigorous interval-arithmetic verification of Fermi Golden Rule constants and absence of embedded eigenvalues for specific $(d,p)$ is an active, feasible target.

## 8. Future Work

- Compute or rigorously bound the Fermi Golden Rule coefficient for the cubic 3D NLS soliton via computer-assisted spectral analysis, thereby removing hypothesis (c) in a concrete case.
- Construct a virial functional in $\mathbb{R}^3$ compatible with the four-parameter modulation group; the obstruction is the boost parameter, absent in real scalar models.
- Classify solutions at *super-threshold* mass–energy levels ($E M$ slightly above $E(Q)M(Q)$), extending Duyckaerts–Roudenko.
- Prove or disprove the existence of non-resolving global solutions ("solitary wave without asymptotic profile") for non-integrable $p$.
- Handle collisions: two solitons with nearly equal velocities. Even in gKdV, inelastic collisions (Martel–Merle) leave a defect; the NLS analogue is unproven.

## 9. Key References

- **[Foundational]** T. Cazenave, P.-L. Lions. *Orbital stability of standing waves for some nonlinear Schrödinger equations.* Communications in Mathematical Physics 85 (1982), 549–561.
- **[Foundational]** M. I. Weinstein. *Nonlinear Schrödinger equations and sharp interpolation estimates.* Communications in Mathematical Physics 87 (1983), 567–576.
- **[Foundational]** M. I. Weinstein. *Modulational stability of ground states of nonlinear Schrödinger equations.* SIAM Journal on Mathematical Analysis 16 (1985), 472–491.
- **[Foundational]** M. Grillakis, J. Shatah, W. Strauss. *Stability theory of solitary waves in the presence of symmetry, I & II.* Journal of Functional Analysis 74 (1987), 160–197; 94 (1990), 308–348.
- **[Foundational]** H. Berestycki, P.-L. Lions. *Nonlinear scalar field equations, I: Existence of a ground state.* Archive for Rational Mechanics and Analysis 82 (1983), 313–345.
- **[Foundational]** M. K. Kwong. *Uniqueness of positive solutions of $\Delta u-u+u^p=0$ in $\mathbb{R}^n$.* Archive for Rational Mechanics and Analysis 105 (1989), 243–266.
- **[SOTA]** A. Soffer, M. I. Weinstein. *Multichannel nonlinear scattering for nonintegrable equations.* Communications in Mathematical Physics 133 (1990), 119–146.
- **[SOTA]** S. Cuccagna. *Stabilization of solutions to nonlinear Schrödinger equations.* Communications on Pure and Applied Mathematics 54 (2001), 1110–1145.
- **[SOTA]** F. Merle, P. Raphaël. *The blow-up dynamic and upper bound on the blow-up rate for critical NLS.* Annals of Mathematics 161 (2005), 157–222.
- **[SOTA]** T. Duyckaerts, S. Roudenko. *Threshold solutions for the focusing 3d cubic Schrödinger equation.* Revista Matemática Iberoamericana 26 (2010), 1–56.
- **[SOTA]** M. Kowalczyk, Y. Martel, C. Muñoz. *Kink dynamics in the $\phi^4$ model: asymptotic stability for odd perturbations in the energy space.* Journal of the AMS 30 (2017), 769–798.
- **[SOTA]** F. Merle, P. Raphaël, I. Rodnianski, J. Szeftel. *On blow up for the energy super critical defocusing nonlinear Schrödinger equations.* Inventiones Mathematicae 227 (2022), 247–413.
- **[Survey]** T. Cazenave. *Semilinear Schrödinger Equations.* Courant Lecture Notes 10, AMS, 2003.
- **[Survey]** T. Tao. *Nonlinear Dispersive Equations: Local and Global Analysis.* CBMS Regional Conference Series 106, AMS, 2006.
- **[Survey]** S. Cuccagna, M. Maeda. *A survey on asymptotic stability of ground states of nonlinear Schrödinger equations.* Discrete and Continuous Dynamical Systems – Series S 14 (2021), 1693–1716.

## 10. Worked Example / Concrete Special Case

**Deciding orbital stability by the slope criterion, for pure-power NLS.**

Take $-\Delta Q+Q=Q^p$ on $\mathbb{R}^d$ with ground state $Q$, and rescale: $Q_\omega(x)=\omega^{\frac{1}{p-1}}Q(\sqrt\omega\,x)$. Then

$$M(Q_\omega)=\int_{\mathbb{R}^d}\omega^{\frac{2}{p-1}}Q(\sqrt\omega x)^2\,dx=\omega^{\frac{2}{p-1}-\frac d2}\|Q\|_{L^2}^2 .$$

Set $\alpha=\frac{2}{p-1}-\frac d2$. Since $d'(\omega)=\frac12M(Q_\omega)$,
$$d''(\omega)=\tfrac12\,\alpha\,\omega^{\alpha-1}\|Q\|_{L^2}^2 .$$
So $\mathrm{sign}\,d''=\mathrm{sign}\,\alpha$, and
$$\alpha>0 \iff \frac{2}{p-1}>\frac d2 \iff p<1+\frac4d .$$

**Cases.**
- $d=1,\ p=3$: $\alpha=1-\tfrac12=\tfrac12>0$ — stable. Explicitly $Q_\omega(x)=\sqrt{2\omega}\,\mathrm{sech}(\sqrt\omega x)$, $M=\int 2\omega\,\mathrm{sech}^2(\sqrt\omega x)dx=4\sqrt\omega$, so $d'(\omega)=2\sqrt{\omega}$, $d''(\omega)=\omega^{-1/2}>0$. Confirms stability, consistent with integrability.
- $d=2,\ p=3$: $\alpha=1-1=0$ — critical, $d''\equiv0$. GSS gives no verdict; the wave is in fact unstable, but only through nonlinear terms (Comech–Pelinovsky 2003), and by Weinstein's sharp Gagliardo–Nirenberg inequality any $u_0$ with $\|u_0\|_2<\|Q\|_2$ is global, while arbitrarily small mass excess above $\|Q\|_2$ permits blow-up.
- $d=3,\ p=3$: $\alpha=1-\tfrac32=-\tfrac12<0$ — $d''<0$, one real unstable eigenvalue of $JL$, exponential orbital instability. Yet the *threshold* dynamics are completely classified (Duyckaerts–Roudenko): the unstable direction produces exactly two special solutions $Q^\pm$, one blowing up in finite time, one scattering, both converging to $e^{it}Q$ as $t\to+\infty$ at rate $e^{-ct}$.

The gap of Section 6 is visible here: in every case above the *orbital* verdict is a one-line computation, whereas whether a perturbed 3D cubic soliton *asymptotically* relaxes to a nearby soliton still requires unverified spectral hypotheses on $L_\pm$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*