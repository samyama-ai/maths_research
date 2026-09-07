---
id: 06-pdes/elliptic-systems-morrey-regularity
title: "Regularity of Elliptic Systems in Morrey Spaces"
topic: 06-pdes
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Regularity of Elliptic Systems in Morrey Spaces

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/elliptic-systems-morrey-regularity` · **Status:** open

## 1. Problem Statement / Conjecture

Second-order elliptic **systems** (vector-valued unknowns) have no maximum principle and no De Giorgi–Nash–Moser theory. Regularity is instead extracted from decay of the local energy on balls — exactly the quantity measured by a Morrey norm. The open problem is to determine the sharp Morrey-scale hypotheses under which weak solutions are continuous, and how large the singular set can be when they are not.

Let $B_1 \subset \mathbb{R}^n$, $n \ge 3$, and let $u \in W^{1,2}(B_1,\mathbb{R}^m)$ solve Rivière's system

$$-\Delta u \;=\; \Omega \cdot \nabla u, \qquad \Omega \in L^2(B_1, so(m)\otimes \Lambda^1\mathbb{R}^n),$$

i.e. $-\Delta u^i = \sum_{j=1}^m \Omega^i_{\ j}\cdot \nabla u^j$ with $\Omega^i_{\ j} = -\Omega^j_{\ i}$ (antisymmetry). Assume the critical Morrey bounds

$$\|\nabla u\|_{L^{2,n-2}(B_1)}^2 + \|\Omega\|_{L^{2,n-2}(B_1)}^2 \;=\; \sup_{B_r(x_0)\subset B_1} r^{2-n}\!\!\int_{B_r(x_0)}\!\!\big(|\nabla u|^2 + |\Omega|^2\big)\,dx \;<\; \Lambda \;<\; \infty .$$

**Conjecture A (borderline regularity without smallness).** Membership in $L^{2,n-2}$ with a *finite* bound $\Lambda$ — not a small one — forces $u$ to be Hölder continuous on the complement of a closed set $\mathrm{Sing}(u)$ with $\mathcal{H}^{n-2}(\mathrm{Sing}(u)) = 0$, and $\mathrm{Sing}(u)$ is $(n-2)$-rectifiable.

**Conjecture B (dimension drop under stationarity).** If in addition $u$ is stationary for a conformally invariant energy (the stress–energy tensor is divergence-free), then $\dim_{\mathcal H}\mathrm{Sing}(u) \le n-3$.

**Conjecture C (linear/quasilinear Morrey scale).** For $-\operatorname{div}(A(x)\nabla u) = \operatorname{div} f$ with $A$ uniformly elliptic and $A \in \mathrm{VMO}$, the implication $f\in L^{p,\lambda} \Rightarrow \nabla u \in L^{p,\lambda}$ persists for the full range $1<p<\infty$, $0\le\lambda<n$, when VMO is relaxed to *small* BMO on the Morrey scale — and one asks for the sharp modulus of continuity of $A$ at which the implication fails.

A complete resolution means either a proof valid for all $n\ge 3$, $m\ge 2$, or a counterexample: a solution with finite (large) critical Morrey norm whose singular set has positive $\mathcal H^{n-2}$-measure.

## 2. Mathematical Foundations

**Morrey and Campanato spaces.** For $1\le p<\infty$, $0\le\lambda\le n$,

$$L^{p,\lambda}(\Omega) = \Big\{ f\in L^p_{loc} : \|f\|_{L^{p,\lambda}}^p = \sup_{x_0\in\Omega,\;0<r<\mathrm{diam}\,\Omega} r^{-\lambda}\!\!\int_{\Omega\cap B_r(x_0)}\!\! |f|^p\,dx <\infty\Big\}.$$

$L^{p,0}=L^p$, $L^{p,n}=L^\infty$. The Campanato space $\mathcal{L}^{p,\lambda}$ replaces $|f|^p$ by $|f-f_{x_0,r}|^p$; **Campanato's theorem** gives the isomorphism

$$\mathcal{L}^{p,\lambda}(\Omega)\;\cong\;C^{0,\alpha}(\overline\Omega),\qquad n<\lambda\le n+p,\quad \alpha=\frac{\lambda-n}{p},$$

on Lipschitz domains. This is the engine: *every* regularity proof below produces a Morrey/Campanato decay $\int_{B_r}|\nabla u|^2 \le C r^{n-2+2\alpha}$ and then invokes Campanato.

**Adams' embedding.** For the Riesz potential $I_\alpha f = |x|^{\alpha-n}*f$, Adams (1975) proved
$$I_\alpha : L^{p,\lambda}\to L^{q,\lambda},\qquad \frac1q=\frac1p-\frac{\alpha}{n-\lambda},\quad 1<p<\tfrac{n-\lambda}{\alpha},$$
so on Morrey scale the effective dimension is $n-\lambda$, not $n$. With $\lambda=n-2$, $p=2$, $\alpha=1$ the effective dimension is $2$ and the system becomes *critical* exactly as in the conformal dimension $n=2$.

**Antisymmetry and gauge.** Rivière (2007) showed that when $\Omega=-\Omega^T$ there exist $\varepsilon(m)>0$ and, for $\|\Omega\|_{L^2(B_1)}<\varepsilon$ in $n=2$, maps $P\in W^{1,2}(B_1,SO(m))$, $\xi\in W^{1,2}(B_1,gl(m)\otimes\Lambda^2)$ with
$$\nabla P\,P^{-1} \;+\; P\,\Omega\,P^{-1} \;=\; \nabla^{\perp}\xi ,$$
turning the system into the conservation law $\operatorname{div}(P^{-1}\nabla u + \nabla^\perp\xi\,P^{-1}u)=0$. Wente's compensated-compactness estimate $\|\phi\|_{L^\infty}+\|\nabla\phi\|_{L^2}\le C\|\nabla a\|_{L^2}\|\nabla b\|_{L^2}$ for $-\Delta\phi=\nabla a\cdot\nabla^\perp b$ closes the argument.

**Model nonlinearity.** Harmonic maps $u:B_1\to N^k\hookrightarrow\mathbb{R}^m$ satisfy $-\Delta u = A(u)(\nabla u,\nabla u)$, which is of the above form with $|\Omega|\le C|\nabla u|$. Stationarity gives the monotonicity formula
$$\frac{d}{dr}\Big( r^{2-n}\!\!\int_{B_r(x_0)}\!\!|\nabla u|^2\Big) = 2r^{2-n}\!\!\int_{\partial B_r(x_0)}\!\!\Big|\frac{\partial u}{\partial r}\Big|^2 \ge 0,$$
which is precisely the statement that the density $\Theta(x_0,r)=r^{2-n}\int_{B_r}|\nabla u|^2$ — the local Morrey quantity — is monotone.

## 3. History & State of the Art (SOTA)

- **1938–1966.** Morrey introduces $L^{p,\lambda}$ and the Dirichlet growth theorem, and proves full regularity for two-dimensional variational systems.
- **1963–1966.** Campanato establishes the $\mathcal{L}^{p,\lambda}\cong C^{0,\alpha}$ isomorphism; Morrey-space methods become the standard replacement for De Giorgi iteration in the vector-valued setting.
- **1968.** De Giorgi's counterexample: $u(x)=x|x|^{-\gamma}$ is an unbounded weak solution of a linear elliptic system with bounded measurable coefficients in $n\ge3$ — full regularity for systems is false, only *partial* regularity is possible.
- **1975.** Adams proves the Morrey–Riesz potential embedding, giving the effective-dimension calculus.
- **1982–1993.** Schoen–Uhlenbeck: minimizing harmonic maps are smooth off a set of dimension $\le n-3$. Bethuel: *stationary* harmonic maps are smooth off a set with $\mathcal{H}^{n-2}=0$.
- **1993.** Chiarenza–Frasca–Longo obtain $W^{2,p}$ theory with VMO coefficients; Di Fazio–Ragusa lift it to Morrey spaces.
- **1999.** Lin's blow-up analysis: for stationary maps into targets with no harmonic spheres, the singular set has dimension $\le n-4$; defect measures are rectifiable.
- **2007–2008.** Rivière's conservation law ($n=2$) and Rivière–Struwe's extension to $n\ge3$: under **smallness** of $\|\Omega\|_{L^{2,n-2}}+\|\nabla u\|_{L^{2,n-2}}$, $u$ is Hölder continuous. This is the current SOTA statement.
- **2013.** Sharp–Topping give direct Morrey decay estimates for Rivière's equation, yielding $\varepsilon$-regularity with explicit constants and compactness.
- **2017.** Naber–Valtorta prove $\mathrm{Sing}(u)$ is $(n-3)$-rectifiable with finite $\mathcal H^{n-3}$ measure for minimizers, and $(n-2)$-rectifiable for stationary maps.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n=2$, $\Omega\in L^2$ antisymmetric | $u\in C^{0,\alpha}_{loc}$, full regularity; no smallness needed after covering | Rivière 2007 |
| $n\ge3$, $\|\Omega\|_{L^{2,n-2}}+\|\nabla u\|_{L^{2,n-2}}<\varepsilon(n,m)$ | $u\in C^{0,\alpha}$ | Rivière–Struwe 2008 |
| Stationary harmonic maps, any $N$ | $\mathcal H^{n-2}(\mathrm{Sing})=0$; $\mathrm{Sing}$ $(n-2)$-rectifiable | Bethuel 1993; Naber–Valtorta 2017 |
| Energy-minimizing maps | $\dim_{\mathcal H}\mathrm{Sing}\le n-3$; $=n-3$ sharp for $N=S^2$, $n=3$ point singularities | Schoen–Uhlenbeck 1982 |
| Stationary maps into $N$ with no harmonic $S^2$ | $\dim_{\mathcal H}\mathrm{Sing}\le n-4$ | Lin 1999 |
| $-\operatorname{div}(A\nabla u)=\operatorname{div} f$, $A\in\mathrm{VMO}$ | $f\in L^{p,\lambda}\Rightarrow \nabla u\in L^{p,\lambda}$, all $1<p<\infty$, $0\le\lambda<n$ | Di Fazio–Ragusa 1993; Byun–Wang 2004 |
| $A$ merely $L^\infty$, $m\ge2$, $n\ge3$ | Only Meyers' gap $\nabla u\in L^{2+\delta,\lambda}$ for small $\delta(\Lambda,n)$ | Meyers; Giaquinta 1983 |
| $A$ merely $L^\infty$, $m\ge2$ | Discontinuous solutions exist | De Giorgi 1968; Šverák–Yan 2002 |

## 5. Principal Obstacles

- **Smallness is not merely technical — it is load-bearing.** The Coulomb gauge $P$ of Rivière's construction exists only when $\|\Omega\|_{L^{2,n-2}}$ is below the Uhlenbeck threshold; for large $\Omega$ the bundle can be topologically non-trivial and no global gauge exists on a ball.
- **Criticality.** With $\lambda=n-2$, the effective dimension is $2$: $\Omega\cdot\nabla u$ sits exactly at the borderline of the Adams embedding, so no $\epsilon$ of integrability is gained per iteration. Standard bootstrapping (Calderón–Zygmund plus Sobolev) is scale-invariant and returns the hypothesis unchanged.
- **No maximum principle.** For systems ($m\ge2$) De Giorgi–Nash–Moser oscillation decay fails; De Giorgi's and Šverák–Yan's examples show the failure is not an artifact of proof technique.
- **Compensated compactness has no Morrey substitute for large norm.** Wente's estimate and the $\mathcal H^1$–$\mathrm{BMO}$ duality of Coifman–Lions–Meyer–Semmes are linear-in-smallness; the corresponding Morrey–Hardy duality ($\mathcal H^{1,\lambda}$ vs. Campanato) lacks a div–curl lemma with constants independent of the energy density.
- **Morrey spaces are non-separable and lack good approximation.** $C^\infty$ is not dense in $L^{p,\lambda}$, the Hardy–Littlewood maximal operator is bounded but Calderón–Zygmund decomposition arguments lose the local-to-global step, and dual/predual structure (Zorko space, Adams–Xiao) is delicate.
- **Defect measures.** Blow-up limits of solutions with large Morrey norm converge weakly with a defect measure $\nu$; showing $\nu$ is carried by an $(n-3)$-dimensional set requires quantitative stratification, which needs stationarity — unavailable for general $\Omega$.

## 6. The Gap

Proven (Section 4) is an $\varepsilon$-regularity statement: continuity **on balls where the critical Morrey norm is below $\varepsilon(n,m)$**. Conjectured (Section 1) is regularity on balls where the norm is merely finite. The gap is the set
$$\Sigma_\varepsilon(u)=\Big\{x_0 : \liminf_{r\to0}\ r^{2-n}\!\!\int_{B_r(x_0)}\!\!(|\nabla u|^2+|\Omega|^2)\,dx \;\ge\;\varepsilon\Big\}.$$
Without a monotonicity formula there is no proof that $\Sigma_\varepsilon$ is $\mathcal H^{n-2}$-null: a covering argument with the Morrey bound alone gives only $\mathcal{H}^{n-2}(\Sigma_\varepsilon)\le C\Lambda/\varepsilon$ — *finiteness*, not vanishing, and no rectifiability. Crossing the gap requires either (i) a gauge construction valid for large $\Omega$, or (ii) an almost-monotonicity formula derived from antisymmetry alone rather than from stationarity.

## 7. Current Research (as of June 2026)

- **Quantitative stratification.** Naber–Valtorta's Reifenberg machinery is being pushed from stationary harmonic maps to general antisymmetric-potential systems, using Jones' $\beta$-numbers on the energy density. Groups at Northwestern, EPFL and SISSA.
- **Nonlinear potential theory.** Kuusi–Mingione pointwise Wolff-potential estimates give a Morrey-scale continuity criterion $\int_0^1 \big(r^{\lambda-n}\int_{B_r}|f|\big)^{1/(p-1)}\frac{dr}{r}<\infty$; extension of this Riesz-potential criterion to systems with antisymmetric structure is active *(frontier — verify)*.
- **Fractional and nonlocal analogues.** Schikorra and coauthors treat $(-\Delta)^{s}u = \Omega\cdot\nabla u$-type systems, where the Morrey scale $L^{2,n-2s}$ replaces $L^{2,n-2}$; the nonlocal gauge is built by commutator estimates rather than Uhlenbeck's theorem.
- **Sharp coefficient regularity.** Determining the exact Dini-type modulus for $A(x)$ separating continuity of $\nabla u$ from Meyers-only integrability, in Morrey norms, on Reifenberg-flat domains.
- **Numerical/computational.** Adaptive FEM producing solutions with prescribed large local density, searching for a counterexample to Conjecture A by exhibiting $\Sigma_\varepsilon$ of positive $\mathcal H^{n-2}$-measure *(frontier — verify)*.

## 8. Future Work

1. Prove an almost-monotonicity formula for $r^{2-n}\int_{B_r}|\nabla u|^2$ using only antisymmetry of $\Omega$ — this would immediately give Conjecture A.
2. Construct Uhlenbeck-type gauges under a *finite* Morrey bound by allowing a nontrivial principal bundle, and quantify the obstruction class.
3. Establish a div–curl lemma in Morrey–Hardy duality with constants independent of the Morrey norm.
4. Settle whether the singular set of a stationary solution to Rivière's system is $(n-3)$-rectifiable when the target has no harmonic spheres — the Lin-type dimension drop in the general-$\Omega$ setting.
5. Search for a De Giorgi–Šverák–Yan-style counterexample tailored to the Morrey borderline: a system with $\Omega\in L^{2,n-2}$, large, and $\mathcal H^{n-2}(\mathrm{Sing})>0$.

## 9. Key References

- **[Foundational]** C. B. Morrey. *On the solutions of quasi-linear elliptic partial differential equations.* Transactions of the AMS **43** (1938), 126–166.
- **[Foundational]** S. Campanato. *Proprietà di hölderianità di alcune classi di funzioni.* Annali della Scuola Normale Superiore di Pisa **17** (1963), 175–188.
- **[Foundational]** E. De Giorgi. *Un esempio di estremali discontinue per un problema variazionale di tipo ellittico.* Bollettino UMI **1** (1968), 135–137.
- **[Foundational]** D. R. Adams. *A note on Riesz potentials.* Duke Mathematical Journal **42** (1975), 765–778.
- **[Book]** M. Giaquinta. *Multiple Integrals in the Calculus of Variations and Nonlinear Elliptic Systems.* Annals of Mathematics Studies 105, Princeton University Press, 1983.
- **[Foundational]** R. Schoen, K. Uhlenbeck. *A regularity theory for harmonic maps.* Journal of Differential Geometry **17** (1982), 307–335.
- **[Foundational]** F. Bethuel. *On the singular set of stationary harmonic maps.* Manuscripta Mathematica **78** (1993), 417–443.
- **[SOTA]** T. Rivière. *Conservation laws for conformally invariant variational problems.* Inventiones Mathematicae **168** (2007), 1–22.
- **[SOTA]** T. Rivière, M. Struwe. *Partial regularity for harmonic maps and related problems.* Communications on Pure and Applied Mathematics **61** (2008), 451–463.
- **[SOTA]** B. Sharp, P. Topping. *Decay estimates for Rivière's equation, with applications to regularity and compactness.* Transactions of the AMS **365** (2013), 2317–2339.
- **[SOTA]** A. Naber, D. Valtorta. *Rectifiable-Reifenberg and the regularity of stationary and minimizing harmonic maps.* Annals of Mathematics **185** (2017), 131–227.
- **[SOTA]** F.-H. Lin. *Gradient estimates and blow-up analysis for stationary harmonic maps.* Annals of Mathematics **149** (1999), 785–829.
- **[Linear theory]** F. Chiarenza, M. Frasca, P. Longo. *$W^{2,p}$-solvability of the Dirichlet problem for nondivergence elliptic equations with VMO coefficients.* Transactions of the AMS **336** (1993), 841–853.
- **[Linear theory]** G. Di Fazio, M. A. Ragusa. *Interior estimates in Morrey spaces for strong solutions to nondivergence form equations with discontinuous coefficients.* Journal of Functional Analysis **112** (1993), 241–256.
- **[Linear theory]** S.-S. Byun, L. Wang. *Elliptic equations with BMO coefficients in Reifenberg domains.* Communications on Pure and Applied Mathematics **57** (2004), 1283–1310.
- **[Counterexample]** V. Šverák, X. Yan. *Non-Lipschitz minimizers of smooth uniformly convex functionals.* Proceedings of the National Academy of Sciences USA **99** (2002), 15269–15276.
- **[Survey]** T. Kuusi, G. Mingione. *Guide to nonlinear potential estimates.* Bulletin of Mathematical Sciences **4** (2014), 1–82.
- **[Survey]** D. R. Adams, J. Xiao. *Morrey spaces in harmonic analysis.* Arkiv för Matematik **50** (2012), 201–230.
- **[Technique]** A. Schikorra. *A remark on gauge transformations and the moving frame method.* Annales de l'IHP – Analyse Non Linéaire **27** (2010), 503–515.

## 10. Worked Example / Concrete Special Case

**The equator map: smallness cannot be dropped from the $\varepsilon$-regularity hypothesis alone.**

Take $n\ge3$, $m=n$, $N=S^{n-1}$, and $u(x)=x/|x|$ on $B_1\subset\mathbb{R}^n$.

*Step 1 — it is a weak solution.* $\partial_i u^j = \delta_{ij}/|x| - x_ix_j/|x|^3$, hence
$$|\nabla u|^2=\frac{n-1}{|x|^2},\qquad \int_{B_1}|\nabla u|^2\,dx = \frac{(n-1)\sigma_{n-1}}{n-2}<\infty \ \text{ for } n\ge3,$$
where $\sigma_{n-1}=|S^{n-1}|$. So $u\in W^{1,2}(B_1,S^{n-1})$. A direct computation gives $\Delta u = -\dfrac{n-1}{|x|^2}\,u = -|\nabla u|^2 u$, the harmonic-map equation into $S^{n-1}$.

*Step 2 — put it in Rivière form.* Set $\Omega^i_{\ j} = u^i\nabla u^j - u^j\nabla u^i$, which is antisymmetric. Since $|u|\equiv1$ forces $u\cdot\nabla u=0$,
$$\Omega\cdot\nabla u \;=\; \sum_j (u^i\nabla u^j - u^j\nabla u^i)\cdot\nabla u^j \;=\; u^i|\nabla u|^2 - \nabla u^i\cdot(u\cdot\nabla u) \;=\; u^i|\nabla u|^2 = -\Delta u^i .$$
So $-\Delta u = \Omega\cdot\nabla u$ exactly, with $|\Omega|^2 = 2(|\nabla u|^2 - |u\cdot\nabla u|^2) = 2|\nabla u|^2$.

*Step 3 — the critical Morrey norm is finite but scale-invariantly large.* Centering at the origin,
$$r^{2-n}\!\!\int_{B_r}\!\!|\Omega|^2 dx = r^{2-n}\!\!\int_{B_r}\!\!\frac{2(n-1)}{|x|^2}dx = r^{2-n}\cdot\frac{2(n-1)\sigma_{n-1}}{n-2}\,r^{n-2} = \frac{2(n-1)\sigma_{n-1}}{n-2},$$
**independent of $r$**. For $n=3$: $\sigma_2=4\pi$, giving $\|\Omega\|^2_{L^{2,1}} = 2\cdot2\cdot4\pi/1 = 16\pi \approx 50.3$, and $\|\nabla u\|^2_{L^{2,1}}=8\pi\approx 25.1$.

*Step 4 — the conclusion fails.* $u$ is discontinuous at $0$: its essential oscillation on every $B_r$ is the full diameter $2$ of $S^{n-1}$. Since the Morrey norm is finite and $x\mapsto u(\lambda x)=u(x)$, no covering or rescaling can reduce it. The Rivière–Struwe threshold is therefore violated for every $n$, and $\varepsilon(n,m) \le 2(n-1)\sigma_{n-1}/(n-2)$ is a hard upper bound on the admissible smallness constant.

*Step 5 — what this does and does not show.* The singular set here is $\{0\}$, of dimension $0 \le n-3$ for $n\ge3$, so the example is consistent with Conjectures A and B. It shows only that the $\varepsilon$-hypothesis cannot simply be deleted from the *proof*; it does not produce a large singular set. Jäger–Kaul showed $u$ is energy-minimizing precisely for $n\ge7$ and unstable for $3\le n\le6$ — so the example is genuinely extremal, and any counterexample to Conjecture A must be built by concentrating such densities along an $(n-2)$-dimensional set rather than at a point. That construction is the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*