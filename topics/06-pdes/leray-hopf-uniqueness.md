---
id: 06-pdes/leray-hopf-uniqueness
title: "Leray Hopf Uniqueness"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Uniqueness of Leray–Hopf Weak Solutions to the 3D Navier–Stokes Equations

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/leray-hopf-uniqueness` · **Status:** open

## 1. Problem Statement / Conjecture

For the incompressible Navier–Stokes system on $\mathbb{R}^3$ or $\mathbb{T}^3$ with viscosity $\nu>0$, divergence-free initial data $u_0 \in L^2$, and **zero external force**, Leray (1934) and Hopf (1951) proved that a global-in-time weak solution satisfying the energy inequality exists. Such solutions are called *Leray–Hopf solutions*.

**Open problem.** Is the Leray–Hopf solution with given $u_0 \in L^2_\sigma(\mathbb{R}^3)$ and $f \equiv 0$ unique?

A complete resolution requires either:

1. **Proof:** show that any two Leray–Hopf solutions $u, v$ with $u(0)=v(0)=u_0$ coincide on their common interval of existence, for all $u_0 \in L^2_\sigma$; or
2. **Disproof:** exhibit $u_0 \in L^2_\sigma$ and two distinct solutions, each in $C_w([0,T];L^2)\cap L^2(0,T;\dot H^1)$ and each satisfying the *strong* energy inequality from $t=0$ (in particular attaining the data strongly in $L^2$).

The distinction from the Clay Millennium regularity problem is essential: a positive answer to regularity implies uniqueness (via weak–strong uniqueness), but uniqueness could conceivably hold even for singular solutions, and non-uniqueness is currently the more widely expected outcome.

## 2. Mathematical Foundations

Let $L^2_\sigma$ be the closure of smooth divergence-free compactly supported fields in $L^2$. The system is
$$\partial_t u - \nu \Delta u + (u\cdot\nabla)u + \nabla p = f, \qquad \nabla\cdot u = 0, \qquad u(\cdot,0)=u_0 .$$

**Definition (Leray–Hopf solution).** $u$ is a Leray–Hopf solution on $[0,T)$ if
$$u \in L^\infty(0,T;L^2_\sigma) \cap L^2(0,T;\dot H^1), \qquad u \in C_w([0,T);L^2),$$
$u$ solves the equation distributionally against divergence-free test fields, and satisfies the **energy inequality**
$$\tfrac12\|u(t)\|_{L^2}^2 + \nu\int_0^t \|\nabla u(s)\|_{L^2}^2\,ds \;\le\; \tfrac12\|u_0\|_{L^2}^2 + \int_0^t\langle f,u\rangle\,ds, \quad \forall t\in[0,T).$$
The **strong** energy inequality replaces $0$ by a.e. $s_0 \le t$ as the initial time.

**Scaling.** If $u$ solves the system, so does $u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)$. A space $X$ is *critical* if $\|u_\lambda(\cdot,0)\|_X = \|u_0\|_X$; examples: $\dot H^{1/2}$, $L^3$, $\dot B^{-1+3/p}_{p,q}$, $BMO^{-1}$. The energy space $L^2(\mathbb{R}^3)$ has scaling exponent $-1/2$: it is **supercritical**, which is exactly why the Leray–Hopf class is too large for the known uniqueness machinery.

**Ladyzhenskaya–Prodi–Serrin (LPS) condition.** If a Leray–Hopf solution additionally satisfies
$$u \in L^p(0,T;L^q(\mathbb{R}^3)), \qquad \frac{2}{p}+\frac{3}{q}=1,\quad 3< q \le \infty,$$
then it is smooth on $(0,T]$ and is the unique Leray–Hopf solution with its data. The endpoint $(p,q)=(\infty,3)$ is included by Escauriaza–Seregin–Šverák (2003).

**Weak–strong uniqueness (Leray–Prodi–Serrin–Lions).** If $v$ is an LPS solution and $u$ any Leray–Hopf solution with the same data, then $u\equiv v$. The proof is a Gronwall estimate on $w=u-v$; see Section 10.

**Partial regularity (Caffarelli–Kohn–Nirenberg, 1982).** For *suitable* weak solutions — those additionally satisfying the local energy inequality
$$\partial_t \tfrac{|u|^2}{2} + \nabla\cdot\Big(\big(\tfrac{|u|^2}{2}+p\big)u\Big) - \nu\Delta\tfrac{|u|^2}{2} + \nu|\nabla u|^2 \le 0$$
in $\mathcal{D}'$ — the singular set $S$ has parabolic Hausdorff measure $\mathcal{P}^1(S)=0$. This constrains, but does not exclude, the singularities that would permit branching.

## 3. History & State of the Art (SOTA)

- **1934 — Leray.** Constructs global weak solutions ("turbulent solutions") in $\mathbb{R}^3$; proves weak–strong uniqueness against $L^p_tL^q_x$ regular solutions and the eventual-regularity/epochs-of-irregularity structure. Explicitly leaves uniqueness open.
- **1951 — Hopf.** Extends the construction to bounded domains via Galerkin approximation.
- **1959–1962 — Prodi, Serrin, Ladyzhenskaya.** The LPS criterion; Ladyzhenskaya (1959) proves uniqueness in 2D outright.
- **1967 — Ladyzhenskaya.** Explicit non-uniqueness *with force* for a rotationally symmetric example, signalling that the energy inequality alone is weak.
- **1982 — Caffarelli–Kohn–Nirenberg.** Partial regularity; suitable weak solutions become the standard object.
- **1997/2001 — Lions–Masmoudi; Furioli–Lemarié-Rieusset–Terraneo.** Uniqueness of mild solutions in $C([0,T];L^3)$ without smallness.
- **2003 — Escauriaza–Seregin–Šverák.** $L^\infty_t L^3_x$ endpoint regularity/uniqueness, via backward-uniqueness for parabolic operators.
- **2014–2015 — Jia–Šverák.** Program for non-uniqueness: construct self-similar and *discretely* self-similar solutions and show that the linearized operator around a $(-1)$-homogeneous solution can have an unstable eigenvalue, yielding two distinct Leray–Hopf solutions from one scale-invariant datum. The remaining input is a spectral condition they could not verify analytically.
- **2017 — Guillod–Šverák.** Numerical evidence that the required unstable eigenvalue exists for concrete axisymmetric data. *(non-rigorous)*
- **2019 — Buckmaster–Vicol (Annals).** Convex integration proves non-uniqueness of *distributional* weak solutions with finite kinetic energy in $C_t H^\beta_x$, $\beta$ small — these do **not** satisfy the energy inequality, hence are not Leray–Hopf.
- **2022 — Albritton–Brué–Colombo (Annals).** Non-uniqueness of **Leray–Hopf** solutions for the *forced* equations, $f \in L^1_t L^2_x$, by making the Vishik unstable-vortex mechanism rigorous. This is the strongest result to date and isolates the force as the last remaining gap.
- **2022 — Cheskidov–Luo (Invent. Math.).** Sharp non-uniqueness in supercritical LPS spaces: non-unique weak solutions in $L^p_t L^\infty_x$ for $p<2$, showing the LPS scaling line is sharp.

## 4. Partial Results / Verified Cases

Uniqueness in the Leray–Hopf class is **proved** for:

- **Dimension 2** (all $u_0\in L^2_\sigma$, all $T$): Ladyzhenskaya (1959), Lions–Prodi (1959). Here $\|u\|_{L^4_{t,x}}\lesssim \|u_0\|_{L^2}$ by Ladyzhenskaya's inequality $\|u\|_{L^4}^2 \le C\|u\|_{L^2}\|\nabla u\|_{L^2}$, so every weak solution is automatically LPS.
- **3D with LPS regularity**: $u\in L^p_tL^q_x$, $2/p+3/q=1$, $q\in(3,\infty]$ (Prodi–Serrin–Ladyzhenskaya), and the endpoint $q=3$, $p=\infty$ (ESS 2003).
- **3D short time / small data in critical spaces**: $u_0 \in \dot H^{1/2}$, $L^3$, or $\|u_0\|_{BMO^{-1}}$ small (Fujita–Kato 1964; Koch–Tataru 2001) — a unique mild solution exists and absorbs all Leray–Hopf solutions.
- **3D large times**: for $t > T_*(\|u_0\|_{L^2},\nu)$ every Leray–Hopf solution is smooth (Leray's eventual regularity), so non-uniqueness can only occur on a compact time set of measure zero (in fact of Hausdorff dimension $\le 1/2$ in $t$).
- **Axisymmetric without swirl** ($u_\theta \equiv 0$): global smoothness (Ladyzhenskaya 1968; Ukhovskii–Yudovich 1968), hence uniqueness.
- **Gradient-type conditions**: one velocity component control, $\nabla u \in L^p_tL^q_x$ with $2/p+3/q=2$, pressure conditions — all yield uniqueness in their respective classes.
- **Forced non-uniqueness**: for $f\in L^1_tL^2_x$, uniqueness is **false** in 3D (Albritton–Brué–Colombo 2022) and in 2D Euler (Vishik; Albritton et al. 2024).

## 5. Principal Obstacles

- **Supercriticality of the energy space.** The a priori bound $u\in L^\infty_tL^2\cap L^2_t\dot H^1$ embeds only into $L^{10/3}_{t,x}$ and $L^p_tL^q_x$ with $2/p+3/q=3/2$ — a full $1/2$ derivative away from the LPS line $=1$. No known interpolation closes this gap; the nonlinearity dominates dissipation at small scales.
- **The uniqueness estimate loses derivatives.** The difference $w=u-v$ obeys $\frac{d}{dt}\|w\|_{L^2}^2 + 2\nu\|\nabla w\|^2 \le 2|\langle (w\cdot\nabla)v, w\rangle|$, and controlling the right side by $\nu\|\nabla w\|^2 + C\|v\|_{L^q}^p\|w\|^2$ *requires* $v$ to be LPS. With only $v \in L^2_t\dot H^1$ the term is exactly borderline and Gronwall fails.
- **Convex integration cannot produce the energy inequality.** The Buckmaster–Vicol / Cheskidov–Luo schemes build solutions by adding highly oscillatory Mikado/intermittent flows; energy is prescribed, not dissipated, and iterates cannot be forced to satisfy $\frac{d}{dt}\frac12\|u\|^2 \le -\nu\|\nabla u\|^2$ with sharp constant. At the LPS line, dissipation beats the intermittency budget — Cheskidov–Luo's $p<2$ threshold is provably sharp.
- **The spectral condition in the Jia–Šverák program is not analytically accessible.** It asks for an unstable eigenvalue of a non-selfadjoint, non-compactly-resolvent operator on a scale-invariant profile; numerics support it but rigorous eigenvalue localization for this operator is unresolved.
- **Removing the force is not a perturbation.** In Albritton–Brué–Colombo the force $f\in L^1_tL^2_x$ carries a $(-3)$-homogeneous singularity at the origin that sustains the unstable background vortex. Absorbing it into the data would require a genuinely self-sustaining unstable similarity profile.

## 6. The Gap

Proved: uniqueness whenever a solution has *any* subcritical or critical extra integrability (LPS through $L^\infty_tL^3$), and non-uniqueness once an $L^1_tL^2_x$ force is allowed. The gap is precisely the strip

$$\Big\{\,2/p+3/q = 1 \Big\} \;\longleftrightarrow\; \Big\{\,2/p+3/q = 3/2 \,\Big\},$$

together with the removal of the force. Two concrete crossing steps:

1. **Toward non-uniqueness:** verify the spectral instability of a $(-1)$-homogeneous (or discretely self-similar) profile rigorously, or build an unforced analogue of the Vishik vortex; then the Jia–Šverák bifurcation supplies two Leray–Hopf solutions from one datum.
2. **Toward uniqueness:** obtain any a priori bound on Leray–Hopf solutions strictly above the $3/2$ line — even $L^p_tL^q_x$ with $2/p+3/q = 3/2 - \varepsilon$ for the *class*, not for individual solutions — which no known method provides.

## 7. Current Research (as of June 2026)

- **Rigorous instability spectra.** Groups around Albritton (Wisconsin), Brué (Bocconi), Colombo (EPFL), and De Lellis (IAS) are pushing the unstable-vortex mechanism toward the unforced 3D case and toward 2D Euler/hypodissipative Navier–Stokes. *(frontier — verify)*
- **Computer-assisted spectral proofs.** Interval-arithmetic verification of the Jia–Šverák eigenvalue condition, following Guillod–Šverák's numerics, is an active line; success would settle non-uniqueness. *(frontier — verify)*
- **Intermittent convex integration at the dissipation threshold.** Cheskidov, Luo, Buckmaster, Vicol and collaborators continue to sharpen non-uniqueness in supercritical LPS classes and for hypodissipative $(-\Delta)^\alpha$, $\alpha<5/4$.
- **Selection principles.** Vanishing-viscosity, stochastic (Flandoli–Romito), and maximal-dissipation selections aim to single out a canonical solution even if uniqueness fails — well-posedness "by selection" rather than by PDE.
- **Regularity criteria in Besov/Morrey and one-component form** continue to shrink the class where non-uniqueness could hide.

## 8. Future Work

- Construct an **unforced** self-similar or discretely self-similar profile whose linearization has an unstable eigenvalue; this is the most concrete path to a negative answer.
- Prove or disprove **uniqueness within the class of suitable weak solutions**, where CKN's $\mathcal{P}^1(S)=0$ is available — is partial regularity enough to force a Gronwall closure?
- Determine whether the Leray–Hopf solution set is a **singleton for a.e. initial datum** with respect to a natural (e.g. Gaussian) measure on $L^2_\sigma$ — generic uniqueness may be provable even if uniqueness is not.
- Extend the sharpness of Cheskidov–Luo down to solutions satisfying the *strong* energy inequality; this would essentially close the problem.

## 9. Key References

- **[Foundational]** J. Leray. *Sur le mouvement d'un liquide visqueux emplissant l'espace.* Acta Mathematica 63 (1934), 193–248.
- **[Foundational]** E. Hopf. *Über die Anfangswertaufgabe für die hydrodynamischen Grundgleichungen.* Mathematische Nachrichten 4 (1951), 213–231.
- **[Foundational]** G. Prodi. *Un teorema di unicità per le equazioni di Navier–Stokes.* Annali di Matematica Pura ed Applicata 48 (1959), 173–182.
- **[Foundational]** J. Serrin. *On the interior regularity of weak solutions of the Navier–Stokes equations.* Archive for Rational Mechanics and Analysis 9 (1962), 187–195.
- **[Foundational]** L. Caffarelli, R. Kohn, L. Nirenberg. *Partial regularity of suitable weak solutions of the Navier–Stokes equations.* Communications on Pure and Applied Mathematics 35 (1982), 771–831.
- **[Foundational]** L. Escauriaza, G. Seregin, V. Šverák. *$L_{3,\infty}$-solutions of Navier–Stokes equations and backward uniqueness.* Russian Mathematical Surveys 58 (2003), 211–250.
- **[SOTA]** T. Buckmaster, V. Vicol. *Nonuniqueness of weak solutions to the Navier–Stokes equation.* Annals of Mathematics 189 (2019), 101–144.
- **[SOTA]** D. Albritton, E. Brué, M. Colombo. *Non-uniqueness of Leray solutions of the forced Navier–Stokes equations.* Annals of Mathematics 196 (2022), 415–455.
- **[SOTA]** A. Cheskidov, X. Luo. *Sharp nonuniqueness for the Navier–Stokes equations.* Inventiones Mathematicae 229 (2022), 987–1054.
- **[SOTA]** H. Jia, V. Šverák. *Local-in-space estimates near initial time.* Inventiones Mathematicae 196 (2014), 233–265; and *Are the incompressible d-dimensional Navier–Stokes equations locally ill-posed in the natural energy space?* Journal of Functional Analysis 268 (2015), 3734–3766.
- **[Survey]** J. C. Robinson, J. L. Rodrigo, W. Sadowski. *The Three-Dimensional Navier–Stokes Equations: Classical Theory.* Cambridge University Press, 2016.
- **[Survey]** P. G. Lemarié-Rieusset. *The Navier–Stokes Problem in the 21st Century.* CRC Press, 2016.
- **[Survey]** C. L. Fefferman. *Existence and smoothness of the Navier–Stokes equation.* Clay Mathematics Institute Millennium Problem description, 2000.

## 10. Worked Example / Concrete Special Case

**Weak–strong uniqueness with $v \in L^4(0,T;L^6)$** (the LPS point $p=4,q=6$: $2/4+3/6=1$).

Let $u$ be Leray–Hopf and $v$ Leray–Hopf with the extra bound, $u(0)=v(0)=u_0$, $\nu=1$, $f=0$. Set $w=u-v$. The classical Leray–Serrin computation combines the energy inequality for $u$, the energy *equality* for $v$ (valid since $v\in L^4_tL^6_x$ justifies testing with $v$), and the equation for $v$ tested with $u$:

$$\tfrac12\|w(t)\|_{L^2}^2 + \int_0^t\|\nabla w\|_{L^2}^2 \;\le\; -\int_0^t \langle (w\cdot\nabla)v,\, w\rangle\,ds .$$

All other trilinear terms cancel because $\langle (a\cdot\nabla)b,b\rangle = 0$ for $\nabla\cdot a=0$.

Estimate the right-hand side with Hölder ($\frac16+\frac13+\frac12=1$) and Gagliardo–Nirenberg $\|w\|_{L^3}\le C\|w\|_{L^2}^{1/2}\|\nabla w\|_{L^2}^{1/2}$:

$$|\langle (w\cdot\nabla)v,w\rangle| \le \|v\|_{L^6}\|\nabla w\|_{L^2}\|w\|_{L^3} \le C\|v\|_{L^6}\|\nabla w\|_{L^2}^{3/2}\|w\|_{L^2}^{1/2}.$$

Young's inequality with exponents $(4/3,4)$ gives, for any $\varepsilon>0$,

$$\le \varepsilon\|\nabla w\|_{L^2}^2 + C_\varepsilon\|v\|_{L^6}^4\,\|w\|_{L^2}^2 .$$

Take $\varepsilon = 1$ to absorb the gradient term:

$$\tfrac12\|w(t)\|_{L^2}^2 \;\le\; C\int_0^t \|v(s)\|_{L^6}^4\,\|w(s)\|_{L^2}^2\,ds .$$

Since $\int_0^T\|v\|_{L^6}^4\,ds =: M<\infty$, Gronwall with $\|w(0)\|_{L^2}=0$ yields $\|w(t)\|_{L^2}^2 \le 0\cdot e^{CM}=0$, so $u\equiv v$ on $[0,T]$.

**Where it breaks.** For a general second Leray–Hopf solution we know only $v\in L^\infty_tL^2\cap L^2_t\dot H^1$, hence by interpolation $v\in L^4_tL^3_x$ — *not* $L^4_tL^6_x$. Repeating the estimate with $\|v\|_{L^3}$ forces $\|w\|_{L^6}\lesssim\|\nabla w\|_{L^2}$ on both remaining factors:

$$|\langle (w\cdot\nabla)v,w\rangle| \le \|v\|_{L^3}\|\nabla w\|_{L^2}\|w\|_{L^6} \le C\|v\|_{L^3}\|\nabla w\|_{L^2}^{2},$$

which is *exactly* the same order as the dissipation $\|\nabla w\|_{L^2}^2$ and can only be absorbed if $\|v(t)\|_{L^3}$ is small — no $\|w\|_{L^2}^2$ factor survives for Gronwall. This one missing power of $\|w\|_{L^2}$, equivalent to the $1/2$-derivative gap $2/p+3/q: 3/2 \to 1$, is the entire open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*