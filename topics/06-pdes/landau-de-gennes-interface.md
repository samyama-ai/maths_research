---
id: 06-pdes/landau-de-gennes-interface
title: "Landau-de Gennes Isotropic-Nematic Interface"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Landau-de Gennes Isotropic-Nematic Interface

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/landau-de-gennes-interface` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

At the nematic–isotropic (NI) transition temperature the Landau–de Gennes (LdG) free energy has two equal-depth wells: the isotropic state $Q=0$ and the uniaxial nematic manifold $\{s_+(n\otimes n-\tfrac13 I): n\in\mathbb S^2\}$. A flat interface with unit normal $e_1$ is described by the minimizing heteroclinic connection of the one-dimensional problem
$$
\sigma \;=\; \inf\Big\{ E[Q] \;:\; Q\in H^1_{loc}(\mathbb R;S_0),\ Q(-\infty)=0,\ Q(+\infty)\in \mathcal N \Big\},
$$
with $E$ given in §2. The problem has three parts, all open in the anisotropic regime $L_2+L_3\neq 0$:

- **(C1) Structure.** Every minimizer is *planar-biaxial*: after a rotation fixing $e_1$, $Q(x)$ is diagonal in a fixed frame $\{e_1,e_2,e_3\}$ for all $x$, and is genuinely biaxial (not of the form $s(x)(n\otimes n-\tfrac13 I)$) whenever $L_2+L_3\neq0$ and the far-field director is not parallel to $e_1$.
- **(C2) Anchoring selection.** The optimal angle $\theta^\ast=\angle(n_\infty,e_1)$ satisfies $\theta^\ast\in\{0,\pi/2\}$ for every admissible $(L_1,L_2,L_3)$ — the quartic LdG model with quadratic elasticity admits **no oblique (tilted) minimizing interface**. Explicitly, $\theta^\ast=\pi/2$ (tangential) for $L_2+L_3>0$ and $\theta^\ast=0$ (homeotropic) for $L_2+L_3<0$.
- **(C3) Uniqueness and stability.** The minimizer is unique up to translation and the residual symmetry group, and is a nondegenerate (spectrally stable modulo translation) solution of the Euler–Lagrange system, so that it can serve as the inner layer in a sharp-interface expansion.

A complete resolution means proving or disproving (C1)–(C3) for all elastic constants in the coercivity range, without smallness assumptions on $|L_2+L_3|/L_1$.

## 2. Mathematical Foundations

Let $S_0=\{Q\in\mathbb R^{3\times3}:Q=Q^{T},\ \operatorname{tr}Q=0\}$ with inner product $Q:P=Q_{ij}P_{ij}$. The bulk potential is
$$
f_b(Q)=\frac{a}{2}\operatorname{tr}Q^2-\frac{b}{3}\operatorname{tr}Q^3+\frac{c}{4}\big(\operatorname{tr}Q^2\big)^2,\qquad b,c>0 .
$$
At the transition temperature $a=\dfrac{b^{2}}{27c}$, and $f_b\ge0$ with $f_b^{-1}(0)=\{0\}\cup\mathcal N$, where
$$
\mathcal N=\Big\{s_+\big(n\otimes n-\tfrac13 I\big):n\in\mathbb S^{2}\Big\},\qquad s_+=\frac{b}{3c}.
$$
The elastic energy density is
$$
f_e(\nabla Q)=\frac{L_1}{2}\,\partial_kQ_{ij}\partial_kQ_{ij}+\frac{L_2}{2}\,\partial_jQ_{ij}\partial_kQ_{ik}+\frac{L_3}{2}\,\partial_kQ_{ij}\partial_jQ_{ik},
$$
coercive on $S_0$-valued gradients iff $L_1>0$ and $L_1+L_2+L_3>0$ (equivalently $\eta:=(L_2+L_3)/L_1>-1$). Note $L_2$ and $L_3$ differ by a null Lagrangian, so only $L_2+L_3$ matters.

For a one-dimensional profile $Q=Q(x)$, $x=x_1$, both anisotropic terms collapse to the same expression, $\partial_jQ_{ij}\partial_kQ_{ik}=\partial_kQ_{ij}\partial_jQ_{ik}=|Q'e_1|^2$, giving the **interface functional**
$$
E[Q]=\int_{\mathbb R}\Big[\frac{L_1}{2}|Q'|^{2}+\frac{L_1\eta}{2}\,|Q'e_1|^{2}+f_b(Q)\Big]\,dx .
$$
The Euler–Lagrange system is the semilinear ODE system on $S_0$
$$
L_1Q''+L_1\eta\,\Pi_{S_0}\!\big(Q''e_1\otimes e_1+e_1\otimes e_1\,Q''\big)/2 \;=\; aQ-b\big(Q^{2}-\tfrac13|Q|^{2}I\big)+c\,|Q|^{2}Q,
$$
$\Pi_{S_0}$ the orthogonal projection onto traceless symmetric matrices. $Q$ is **uniaxial** if two eigenvalues coincide, equivalently the biaxiality parameter
$$
\beta(Q)=1-\frac{6\,(\operatorname{tr}Q^{3})^{2}}{(\operatorname{tr}Q^{2})^{3}}
$$
vanishes; $\beta\in[0,1]$. The relevant background results are: Modica–Sternberg $\Gamma$-convergence of $\varepsilon^{-1}\!\int(\varepsilon^2 f_e+f_b)$ to a weighted perimeter with anisotropic surface tension $\sigma(\nu)$ obtained from the cell problem above; and the Majumdar–Zarnescu analysis of the LdG-to-Oseen–Frank limit, which supplies the uniform $L^\infty$ bound $|Q|\le\sqrt{2/3}\,s_+$ used for compactness.

## 3. History & State of the Art (SOTA)

- **1970s–80s (physics).** De Gennes introduced the $Q$-tensor expansion; the NI interface profile with a scalar order parameter (the $L_2=L_3=0$, fixed-director reduction) is the classical Cahn–Hilliard/Allen–Cahn double well. Sheng (1982) computed order-parameter layers at surfaces. Faetti–Palleschi (1984) measured **oblique** anchoring at the free NI interface of cyanobiphenyls, incompatible with (C2) — evidence that quadratic elasticity is insufficient for real materials.
- **1997.** Popa-Nita, Sluckin and Wheeler gave the systematic biaxial analysis of the planar NI interface, showing numerically that biaxiality is generated in the layer whenever $\eta\neq0$ and computing $\sigma(\theta)$; they found $\theta^\ast\in\{0,\pi/2\}$ in the quartic model, consistent with (C2).
- **2010.** Majumdar–Zarnescu (ARMA) established the analytic framework: maximum principle, $\varepsilon\to0$ limits, and the failure of uniaxiality for critical points.
- **2015.** Lamy proved a rigidity theorem: for $\eta\neq0$, any uniaxial solution $Q=s(n\otimes n-\tfrac13 I)$ of the LdG system with $s$ nonconstant must have $n$ constant and, in the 1D setting, $n\parallel e_1$ or $n\perp e_1$ with additional constraints. This turns "biaxiality is generated" from a numerical observation into a theorem for a broad class.
- **2017.** Park, Wang, P. Zhang and Z. Zhang gave the first rigorous existence and structure theory for the minimizing NI heteroclinic: existence of minimizers, exponential convergence to the wells, and — under a smallness/sign condition on $\eta$ — the planar-diagonal structure and the dichotomy $\theta^\ast\in\{0,\pi/2\}$.
- **2020.** Golovaty–Novack–Sternberg–Venkatraman analyzed a model problem with highly disparate elastic constants ($L_1\to0$ relative to the anisotropic term), identifying the $\Gamma$-limit and showing that the layer structure degenerates and new "wall" energies appear.

## 4. Partial Results / Verified Cases

- **Isotropic elasticity, $\eta=0$.** Fully solved. The minimizer is uniaxial with constant director, $Q=s(x)(n\otimes n-\tfrac13 I)$, $s(x)=s_+\big(1+e^{-\lambda x}\big)^{-1}$, $\lambda=b/(3\sqrt{3cL_1})$, and $\sigma_0=\frac{s_+^3}{9}\sqrt{L_1c/3}$, independent of $\nu$ and $n_\infty$: the surface tension is isotropic and the sharp-interface limit is the (unweighted) minimal-perimeter problem.
- **Homeotropic branch, all $\eta>-1$.** The ansatz $Q=s(x)(e_1\otimes e_1-\tfrac13 I)$ solves the full Euler–Lagrange system exactly for every $\eta$, with $\sigma_{\mathrm{hom}}=\sigma_0\sqrt{1+\tfrac{2}{3}\eta}$ (see §10). It is the global minimizer for $\eta<0$ small.
- **Existence and decay, all admissible $L_i$.** Minimizers exist, are smooth, satisfy $|Q|\le\sqrt{2/3}\,s_+$, and converge exponentially to the two wells (Park–Wang–Zhang–Zhang 2017).
- **Small anisotropy.** For $|\eta|$ below an explicit threshold depending on $(b,c)$, (C1) and (C2) hold: minimizers are diagonal in a fixed frame, biaxial when $\eta\neq0$ and $\theta^\ast=\pi/2$, with $\theta^\ast$ selected by the sign of $\eta$.
- **Two-dimensional / reduced $Q$.** For $Q$ constrained to the 2×2 traceless symmetric sector (planar LdG, Golovaty–Montero 2014), the interface problem reduces to a two-component Allen–Cahn system and the connecting orbit is unique up to translation.
- **Dynamics.** For the isotropic-elasticity Beris–Edwards/LdG flow, Fei–Wang–Zhang–Zhang (2015) rigorously justified the sharp-interface limit to a two-phase free-boundary problem on a finite time interval, using the $\eta=0$ profile as the inner layer.

## 5. Principal Obstacles

- **No maximum/comparison principle for the tensor system.** The equation is a strongly coupled 5-component system; scalar Allen–Cahn tools (sliding method, Modica's gradient bound, monotonicity of the profile) have no known tensorial analogue once $\eta\neq0$, because the anisotropic term $\Pi_{S_0}(Q''e_1\otimes e_1+\cdots)$ is not a multiple of the identity in $S_0$ and breaks $O(3)$ equivariance down to $O(2)\times\mathbb Z_2$.
- **Loss of symmetry-reduction.** For $\eta=0$ the energy is invariant under conjugation by all of $SO(3)$, which lets one project onto a uniaxial invariant subspace. For $\eta\neq0$ only rotations about $e_1$ survive; the "planar/diagonal" ansatz is a *conjecture*, not a consequence of symmetry, and no reflection-rearrangement inequality is known to enforce it.
- **The order parameter vanishes.** On the isotropic side $Q\to0$, so the eigenframe is undefined and $\beta$ is singular; director-based (Oseen–Frank) methods and any argument requiring $|Q|$ bounded below break down exactly where the anchoring competition is decided.
- **Nonconvexity in the wrong variables.** $f_b$ is not convex, and the energy is not a perturbation of a convex functional in any known coordinate system, so uniqueness of the heteroclinic (usually obtained by convexity or by a Hamiltonian/shooting argument in one unknown) is unavailable for a 5-dimensional phase space where the connecting orbit is a codimension-2 intersection of stable/unstable manifolds.
- **Degenerate limits.** As $\eta\to-1^+$ or $\eta\to\infty$ the quadratic form loses coercivity in one direction, the layer splits into multiple scales, and $\Gamma$-limits change type (Golovaty et al. 2020); uniform-in-$\eta$ estimates are missing.

## 6. The Gap

Proven: existence, decay, the exact $\eta=0$ solution, the exact homeotropic branch for all $\eta$, Lamy's rigidity ruling out nonconstant-director uniaxial solutions, and (C1)–(C2) for $|\eta|$ small. Conjectured: the same statements for **all** $\eta>-1$.

The precise missing step is a **global reduction lemma**: show that any minimizer $Q$ can be conjugated so that $Q(x)$ is simultaneously diagonalizable in a single $x$-independent frame containing $e_1$. Equivalently, show that the off-diagonal components $Q_{12},Q_{13},Q_{23}$ of a minimizer vanish identically. For small $|\eta|$ this follows from a perturbative Lyapunov–Schmidt argument around the $\eta=0$ orbit, which is nondegenerate; the argument gives no control once the linearization's spectral gap can close, which cannot presently be excluded for large $|\eta|$. A second, smaller gap is the strict inequality $\sigma(\pi/2)<\sigma(\theta)<\sigma(0)$ for $0<\theta<\pi/2$ and $\eta>0$: only the endpoint values are computable in closed form, and $\theta\mapsto\sigma(\theta)$ is not known to be monotone.

## 7. Current Research (as of June 2026)

- **Beijing/Hangzhou school (P. Zhang, Z. Zhang, W. Wang).** Extending the 2017 structure theorem to moderate $\eta$ via refined spectral analysis of the linearized operator around the homeotropic branch; also higher-order sharp-interface expansions for the Beris–Edwards system with unequal elastic constants.
- **Toulouse / Bath / Oxford (Lamy, Majumdar, Ball).** Rigidity and symmetry for $Q$-tensor systems; quantitative versions of "biaxiality is forced" with lower bounds on $\int\beta(Q)$ in terms of $|\eta|$. *(frontier — verify)*
- **Akron / Indiana / Purdue (Golovaty, Sternberg, Novack, Venkatraman, Phillips).** $\Gamma$-limits with disparate elastic constants and the emergence of anisotropic surface tension $\sigma(\nu)$ and interior walls.
- **Beyond quadratic elasticity.** Because (C2) forbids oblique anchoring while experiments show $\theta^\ast\approx 60^\circ$–$70^\circ$ for MBBA and 5CB, work continues on the cubic term $L_4 Q_{lk}\partial_lQ_{ij}\partial_kQ_{ij}$, which produces tilted minimizers but renders the energy unbounded below (Ball–Majumdar); regularized/constrained variants using the Ball–Majumdar singular potential $f_{BM}$, which confines eigenvalues to $(-1/3,2/3)$, are the main proposed fix. *(frontier — verify)*
- **Numerics.** High-accuracy spectral continuation in $\eta$ and in $\theta$, and molecular-field (Onsager/Maier–Saupe) computations of $\sigma(\theta)$ used to calibrate whether the $\theta^\ast$ dichotomy is a modelling artifact.

## 8. Future Work

1. Prove the diagonalization lemma of §6 by a rearrangement or reflection argument adapted to $S_0$-valued maps, or produce a numerical counterexample at large $\eta$ with a genuinely non-diagonal minimizer.
2. Establish nondegeneracy of the connecting orbit for all $\eta>-1$; this is the input needed to build the inner layer in a sharp-interface expansion with anisotropic elasticity.
3. Compute $\sigma(\nu,\theta)$ and prove convexity of the associated Wulff shape, which would give a well-posed anisotropic mean-curvature flow as the $\varepsilon\to0$ dynamics.
4. Settle the oblique-anchoring question in the Ball–Majumdar model with an $L_4$ term: is there a parameter regime with a stable tilted interface and energy bounded below?
5. Extend to curved interfaces and to interfaces meeting a boundary or a disclination line, where the anchoring dichotomy interacts with defect core structure.

## 9. Key References

- **[Foundational]** P. G. de Gennes and J. Prost. *The Physics of Liquid Crystals*, 2nd ed. Oxford University Press, 1993.
- **[Foundational]** J. L. Ericksen. *Liquid crystals with variable degree of orientation.* Archive for Rational Mechanics and Analysis 113 (1991), 97–120.
- **[Foundational]** E. G. Virga. *Variational Theories for Liquid Crystals.* Chapman & Hall, 1994.
- **[Physics]** P. Sheng. *Boundary-layer phase transition in nematic liquid crystals.* Physical Review A 26 (1982), 1610–1617.
- **[Experiment]** S. Faetti and V. Palleschi. *Nematic-isotropic interface of some members of the homologous series of 4-cyano-4'-(n-alkyl)biphenyl liquid crystals.* Physical Review A 30 (1984), 3241–3251.
- **[Physics]** V. Popa-Nita, T. J. Sluckin and A. A. Wheeler. *Statics and kinetics at the nematic-isotropic interface: effects of biaxiality.* Journal de Physique II (France) 7 (1997), 1225–1243.
- **[Foundational]** A. Majumdar and A. Zarnescu. *Landau–De Gennes theory of nematic liquid crystals: the Oseen–Frank limit and beyond.* Archive for Rational Mechanics and Analysis 196 (2010), 227–280.
- **[Foundational]** J. M. Ball and A. Majumdar. *Nematic liquid crystals: from Maier-Saupe to a continuum theory.* Molecular Crystals and Liquid Crystals 525 (2010), 1–11.
- **[SOTA]** X. Lamy. *Uniaxial symmetry in nematic liquid crystals.* Annales de l'Institut Henri Poincaré C, Analyse Non Linéaire 32 (2015), 1125–1144.
- **[SOTA]** J. Park, W. Wang, P. Zhang and Z. Zhang. *On minimizers for the isotropic–nematic interface problem.* Calculus of Variations and Partial Differential Equations 56 (2017), article 41.
- **[SOTA]** M. Fei, W. Wang, P. Zhang and Z. Zhang. *Dynamics of the nematic-isotropic sharp interface for the liquid crystal flow.* SIAM Journal on Applied Mathematics 75 (2015), 1700–1724.
- **[SOTA]** D. Golovaty, M. Novack, P. Sternberg and R. Venkatraman. *A model problem for nematic-isotropic transitions with highly disparate elastic constants.* Archive for Rational Mechanics and Analysis 236 (2020), 1739–1805.
- **[Related]** D. Golovaty and A. Montero. *On minimizers of a Landau–de Gennes energy functional on planar domains.* Archive for Rational Mechanics and Analysis 213 (2014), 447–490.
- **[Classical]** L. Modica. *The gradient theory of phase transitions and the minimal interface criterion.* Archive for Rational Mechanics and Analysis 98 (1987), 123–142.
- **[Survey]** W. Wang, P. Zhang and Z. Zhang. *Modelling and computation of liquid crystals.* Acta Numerica 30 (2021), 765–851.

## 10. Worked Example / Concrete Special Case

**Step 1 — the isotropic profile ($\eta=0$).** Insert $Q=s(x)(n\otimes n-\tfrac13I)$, $|n|=1$. Then $\operatorname{tr}Q^2=\tfrac23 s^2$, $\operatorname{tr}Q^3=\tfrac29 s^3$, $|Q'|^2=\tfrac23(s')^2$, and at $a=b^2/(27c)$,
$$
f_b=\frac{a}{3}s^{2}-\frac{2b}{27}s^{3}+\frac{c}{9}s^{4}=\frac{c}{9}\,s^{2}(s-s_+)^{2},\qquad s_+=\frac{b}{3c}.
$$
So $E[Q]=\int \tfrac{L_1}{3}(s')^2+\tfrac{c}{9}s^2(s-s_+)^2$. Equipartition gives $s'=\sqrt{c/(3L_1)}\,s(s_+-s)$, i.e.
$$
s(x)=\frac{s_+}{1+e^{-\lambda x}},\qquad \lambda=s_+\sqrt{\frac{c}{3L_1}}=\frac{b}{3\sqrt{3cL_1}} .
$$
Surface tension: $\sigma_0=\tfrac{2L_1}{3}\int(s')^2dx=\tfrac{2L_1}{3}\sqrt{\tfrac{c}{3L_1}}\int_0^{s_+}s(s_+-s)\,ds=\dfrac{s_+^{3}}{9}\sqrt{\dfrac{L_1c}{3}}$. It does not depend on $n$: anchoring is degenerate at $\eta=0$.

**Step 2 — switching on $\eta$, two uniaxial competitors.** With $Q=s(x)(n\otimes n-\tfrac13I)$ and $Q'=s'(n\otimes n-\tfrac13 I)$:

| $n$ | $Q'e_1$ | $|Q'e_1|^2$ | effective stiffness | surface tension |
|---|---|---|---|---|
| $e_1$ (homeotropic) | $\tfrac23 s'\,e_1$ | $\tfrac49 (s')^2$ | $L_1(1+\tfrac23\eta)$ | $\sigma_0\sqrt{1+\tfrac23\eta}$ |
| $e_3$ (tangential) | $-\tfrac13 s'\,e_1$ | $\tfrac19 (s')^2$ | $L_1(1+\tfrac16\eta)$ | $\le\sigma_0\sqrt{1+\tfrac16\eta}$ |

(Each row: total gradient coefficient $\tfrac{L_1}{3}\big(1+\tfrac{3\eta}{2}|Q'e_1|^2/(s')^2\big)$, and $\sigma\propto\sqrt{L_{\mathrm{eff}}}$ since rescaling $x\mapsto x\sqrt{L_{\mathrm{eff}}/L_1}$ maps one profile to the other.) For $\eta>0$ the tangential competitor is strictly cheaper, for $\eta<0$ the homeotropic one is — this is the mechanism behind (C2).

**Step 3 — biaxiality is forced.** Check which ansatz solves the Euler–Lagrange system. For $n=e_1$: $Q''e_1=\tfrac23 s''e_1$, and $\Pi_{S_0}(\tfrac23 s'' e_1\otimes e_1)=\tfrac23 s''(e_1\otimes e_1-\tfrac13 I)$ — proportional to the ansatz direction, so the uniaxial homeotropic profile is an *exact* solution for every $\eta$, with $s$ as in Step 1 and $\lambda$ rescaled by $(1+\tfrac23\eta)^{-1/2}$. For $n=e_3$: $Q''e_1=-\tfrac13 s''e_1$, so the anisotropic term contributes $-\tfrac13 s''(e_1\otimes e_1-\tfrac13I)$, which is **not** parallel to $(e_3\otimes e_3-\tfrac13 I)$. The uniaxial tangential ansatz therefore fails to solve the system whenever $\eta\ne0$; the true tangential connection must activate a second component. Writing $Q=\operatorname{diag}(q_1,q_2,-q_1-q_2)$ with $|Q'e_1|^2=(q_1')^2$, the layer solves the two-component system
$$
L_1\big(2q_1''+q_2''\big)+L_1\eta\,\tfrac{2}{3}\big(2q_1''+q_2''\big)\big|_{\text{proj}}=\partial_{q_1}f_b,\qquad L_1\big(2q_2''+q_1''\big)=\partial_{q_2}f_b,
$$
connecting $(0,0)$ to $(-s_+/3,-s_+/3)$. Along this orbit $q_1\neq q_2$ for $\eta\neq0$, so $\beta(Q)>0$ on an open set: the minimizing NI interface is biaxial, with a thin biaxial layer of thickness $O(\lambda^{-1})$ and peak biaxiality $O(|\eta|)$ for small $\eta$. Proving that this diagonal, two-component orbit is the global minimizer for *all* $\eta>-1$ — rather than only for $|\eta|$ small — is exactly the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*