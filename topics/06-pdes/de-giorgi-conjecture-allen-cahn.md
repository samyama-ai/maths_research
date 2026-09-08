---
id: 06-pdes/de-giorgi-conjecture-allen-cahn
title: "De Giorgi Conjecture for the Allen–Cahn Equation in Dimensions Nine and Above"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# De Giorgi Conjecture for the Allen–Cahn Equation in Dimensions Nine and Above

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/de-giorgi-conjecture-allen-cahn` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

De Giorgi (1978) conjectured: let $u \in C^2(\mathbb{R}^n)$ solve the Allen–Cahn equation
$$\Delta u + u - u^3 = 0 \quad \text{in } \mathbb{R}^n,$$
with $|u| < 1$ and $\partial_{x_n} u > 0$. Then all level sets $\{u = \lambda\}$ are parallel hyperplanes, i.e. $u(x) = \tanh\!\big(\tfrac{a\cdot x + b}{\sqrt 2}\big)$ for some unit vector $a$ with $a_n>0$ and $b \in \mathbb{R}$ — "at least for $n \le 8$".

The parenthetical dimension restriction is the crux. The problem, as tracked here, has three live components:

1. **$n \ge 9$: the conjecture is false** (del Pino–Kowalczyk–Wei, 2011). Open: *classify* the non-planar monotone solutions — moduli, uniqueness, Morse index, and whether the level sets of every monotone solution are asymptotic to a minimal graph.
2. **$4 \le n \le 8$: open without an auxiliary hypothesis.** Savin (2009) proved the conjecture in these dimensions under the extra assumption $\lim_{x_n \to \pm\infty} u(x', x_n) = \pm 1$ pointwise in $x'$. Removing this hypothesis is open.
3. **Stable solutions.** Is every *stable* solution (not merely monotone) one-dimensional for $3 \le n \le 7$? Known false for $n \ge 8$.

A complete resolution means: a classification theorem for monotone entire solutions in each $n$, and the sharp dimension threshold for the stable-solution version.

## 2. Mathematical Foundations

**Energy.** With double-well potential $W(u) = \tfrac14 (1-u^2)^2$, solutions are critical points of
$$E_\Omega(u) = \int_\Omega \Big( \tfrac12 |\nabla u|^2 + W(u) \Big)\,dx ,$$
whose Euler–Lagrange equation is $\Delta u = W'(u) = u^3 - u$.

**Stability.** $u$ is *stable* if the second variation is nonnegative:
$$Q_u(\varphi) = \int_{\mathbb{R}^n} \big( |\nabla \varphi|^2 + W''(u)\varphi^2 \big) dx \ge 0 \quad \forall \varphi \in C_c^\infty(\mathbb{R}^n),\qquad W''(u)=3u^2-1 .$$
Monotonicity implies stability: $\varphi = \partial_{x_n} u > 0$ solves the linearized equation $\Delta \varphi = W''(u)\varphi$, and a positive solution of the linearized problem forces $Q_u \ge 0$ (Berestycki–Caffarelli–Nirenberg; Ambrosio–Cabré). $u$ is a *global minimizer* (De Giorgi minimizer) if $E_\Omega(u) \le E_\Omega(u+\psi)$ for all $\psi \in C_c^\infty(\Omega)$, all bounded $\Omega$. Minimizer $\Rightarrow$ stable; the converse is false.

**Modica estimate.** Any bounded entire solution satisfies the pointwise gradient bound
$$\tfrac12 |\nabla u|^2 \le W(u) \quad \text{in } \mathbb{R}^n,$$
with equality at one point forcing $u$ to be one-dimensional (Modica, 1985).

**$\Gamma$-convergence and the minimal-surface link.** Rescale $u_\varepsilon(x) = u(x/\varepsilon)$; then
$$E_\varepsilon(v) = \int_\Omega \Big( \tfrac{\varepsilon}{2}|\nabla v|^2 + \tfrac1\varepsilon W(v) \Big) dx \ \xrightarrow{\ \Gamma\ }\ c_0\, \mathrm{Per}_\Omega(\{v = 1\}),\qquad c_0 = \int_{-1}^{1}\sqrt{2W(s)}\,ds = \tfrac{2\sqrt2}{3},$$
(Modica–Mortola 1977; Modica 1987). Level sets of minimizers converge to minimal hypersurfaces; monotonicity in $x_n$ makes the limit interface a **minimal graph** over $\mathbb{R}^{n-1}$.

**Bernstein theorem.** Every entire minimal graph over $\mathbb{R}^{m}$ is affine for $m \le 7$ (Bernstein, De Giorgi, Almgren, Simons); Bombieri–De Giorgi–Giusti (1969) built a non-affine entire minimal graph over $\mathbb{R}^8$ in $\mathbb{R}^9$. With $m = n-1$, this reproduces exactly De Giorgi's threshold $n \le 8$.

**Simons cone.** $\mathcal{C}_{m,m} = \{x_1^2+\dots+x_m^2 = x_{m+1}^2+\dots+x_{2m}^2\} \subset \mathbb{R}^{2m}$ is a stable, area-minimizing singular cone precisely for $2m \ge 8$.

## 3. History & State of the Art (SOTA)

- **1978.** De Giorgi states the conjecture in *Convergence problems for functionals and operators* (Proc. Int. Meeting on Recent Methods in Nonlinear Analysis, Rome 1978), explicitly as the PDE analogue of the Bernstein problem.
- **1980s.** Modica–Mortola $\Gamma$-convergence and Modica's gradient bound supply the geometric dictionary; Caffarelli–Córdoba (1995) prove uniform density estimates giving locally uniform convergence of level sets.
- **1997–2000.** Berestycki–Caffarelli–Nirenberg reduce the problem to a Liouville property for the linearized operator. **$n=2$**: Ghoussoub–Gui (1998). **$n=3$**: Ambrosio–Cabré (2000).
- **2004.** Jerison–Monneau reduce a counterexample in $\mathbb{R}^{n}$ to the existence of a bounded, even, non-constant global minimizer in $\mathbb{R}^{n-1}$.
- **2009.** Savin proves the conjecture for $4 \le n \le 8$ under the limit hypothesis, via a flatness/improvement-of-flatness theorem for level sets, and separately proves every global minimizer in $\mathbb{R}^n$, $n\le 7$, is one-dimensional.
- **2011.** del Pino–Kowalczyk–Wei construct a monotone, non-planar solution in $\mathbb{R}^9$ (and every $n\ge 9$) by infinite-dimensional Lyapunov–Schmidt reduction along a dilated BDG graph. The conjecture is **false** for $n \ge 9$.
- **2013–2017.** Pacard–Wei build a stable non-planar solution in $\mathbb{R}^8$ modelled on $\mathcal{C}_{4,4}$; Liu–Wang–Wei construct non-planar *global minimizers* in $\mathbb{R}^n$, $n \ge 8$.

## 4. Partial Results / Verified Cases

| Regime | Statement | Status |
|---|---|---|
| $n = 2$ | Monotone (even just stable) $\Rightarrow$ 1D | Proved: Ghoussoub–Gui (1998); Berestycki–Caffarelli–Nirenberg |
| $n = 3$ | Monotone $\Rightarrow$ 1D | Proved: Ambrosio–Cabré (2000) |
| $4 \le n \le 8$ | Monotone **and** $\lim_{x_n\to\pm\infty} u = \pm1$ $\Rightarrow$ 1D | Proved: Savin (2009) |
| $n \le 7$, minimizers | Global minimizer $\Rightarrow$ 1D | Proved: Savin (2009) |
| all $n$, Gibbons version | $u \to \pm1$ *uniformly* in $x'$ $\Rightarrow$ 1D | Proved independently: Barlow–Bass–Gui (2000); Berestycki–Hamel–Monneau (2000); Farina (1999) |
| $n \ge 9$ | Monotone non-planar solutions exist | Proved: del Pino–Kowalczyk–Wei (2011) — conjecture false |
| $n \ge 8$, minimizers | Non-planar global minimizers exist | Pacard–Wei (2013, $n=8$); Liu–Wang–Wei (2017, $n\ge8$) |
| $\mathbb{R}^{2m}$ saddle solutions | Unstable for $2m \le 6$ (Cabré–Terra); unique and stable for $2m \ge 14$ (Cabré) | Dimensions $2m = 8,10,12$ partially settled |
| $4 \le n \le 8$, no limit hypothesis | — | **Open** |
| $3 \le n \le 7$, stable $\Rightarrow$ 1D | — | **Open** |

## 5. Principal Obstacles

- **Liouville arguments stop at $n=3$.** The Berestycki–Caffarelli–Nirenberg/Ambrosio–Cabré route needs the energy growth $E_{B_R}(u) = O(R^{n-1})$ *together with* a Liouville theorem for $\mathrm{div}(\varphi^2 \nabla \sigma) = 0$ requiring $\int_{B_R} \varphi^2 \sigma^2 = O(R^2)$. Monotonicity gives only $O(R^{n-1})$, which matches $O(R^2)$ exactly at $n = 3$. No known refinement closes the deficit for $n \ge 4$.
- **Flatness theory is quantitative but local.** Savin's improvement-of-flatness argument needs the level set to be a graph *with vanishing slope at infinity*; this is precisely what the hypothesis $\lim u = \pm 1$ supplies. Without it, the limits $u^\pm(x') = \lim_{x_n\to\pm\infty} u$ are global minimizers in $\mathbb{R}^{n-1}$ which are known to be 1D only for $n-1 \le 7$, and being 1D does not force them constant.
- **The geometry genuinely changes at $n=9$.** Any proof valid for $n\le 8$ must use dimension in an essential way — it must fail on the BDG graph. Methods that are dimension-blind (maximum principles, sliding, moving planes, energy comparison) cannot suffice.
- **Rigidity vs. flexibility for $n \ge 9$.** The counterexamples are perturbative: they live in a small neighbourhood of a *dilated* BDG graph $\varepsilon^{-1}\Gamma$ and are constructed by Lyapunov–Schmidt reduction over an infinite-dimensional kernel (Jacobi fields of $\Gamma$). The reduction gives existence but almost no information about the full solution set; a classification would need a non-perturbative structure theorem for minimal graphs over $\mathbb{R}^8$, which is itself open.
- **Stability without minimality.** Stability is a scalar inequality; minimality is a comparison over all competitors. There is no known device converting $Q_u\ge0$ into minimality for $n\ge3$, so Savin's minimizer classification does not transfer to stable solutions.

## 6. The Gap

Three explicit steps separate Section 4 from a complete theory.

1. **Remove Savin's limit hypothesis for $4 \le n \le 8$.** Concretely: show that a monotone bounded solution in $\mathbb{R}^n$, $n\le8$, cannot have non-constant limits $u^\pm$. Equivalently (Jerison–Monneau), rule out bounded, even, non-constant global minimizers in $\mathbb{R}^{n-1}$, $n-1 \le 7$ — consistent with, but not implied by, Savin's 1D classification of minimizers.
2. **Close the stability interval $3 \le n \le 7$.** Prove or disprove: stable $\Rightarrow$ 1D. The counterexample at $n=8$ (Simons cone) suggests $7$ is the sharp threshold, matching the Bernstein/Simons dimension, but no proof exists past $n=2$.
3. **Classify the $n \ge 9$ solution set.** Is every monotone entire solution in $\mathbb{R}^n$ asymptotic, after rescaling, to a (possibly affine) entire minimal graph over $\mathbb{R}^{n-1}$? Are the del Pino–Kowalczyk–Wei solutions non-degenerate and unique in their asymptotic class?

## 7. Current Research (as of June 2026)

- **Chile/Chinese Univ. of Hong Kong/UBC axis** (del Pino, Wei, Kowalczyk, Liu): gluing and infinite-dimensional reduction; extensions to fractional Allen–Cahn $(-\Delta)^s u = u - u^3$, where the threshold dimension is governed by nonlocal minimal surfaces and the sharp $n$ for the De Giorgi statement is unresolved for $s \ne 1/2$, $n \ge 4$. *(frontier — verify)*
- **Barcelona school** (Cabré, and collaborators on saddle-shaped and stable solutions): sharp stability thresholds, Hardy-type inequalities on cones, and the $2m \in \{8,10,12\}$ residual cases for saddle solutions.
- **Regularity/geometric-measure-theory side** (Savin, Chodosh, Mantoulidis, Wang–Wei): min-max and Allen–Cahn approximations of minimal hypersurfaces; multiplicity-one and curvature estimates for stable Allen–Cahn solutions, which feed directly into the stable-classification problem for $n \le 7$. *(frontier — verify)*
- **Surveys** keeping the ledger: Farina–Valdinoci (2009); Chan–Wei (2018).

## 8. Future Work

- Develop a *non-perturbative* asymptotic theory for monotone solutions in $\mathbb{R}^9$: prove that the blow-down $\lim_{\varepsilon\to0}\{u(\cdot/\varepsilon)=0\}$ is always an area-minimizing graph, then transfer known minimal-graph classification results.
- Attack step 1 of the Gap via a refined Jerison–Monneau reduction combined with Savin's curvature estimates for minimizers in $\mathbb{R}^7$.
- Prove sheeting/curvature estimates for *stable* (not minimizing) Allen–Cahn solutions in $\mathbb{R}^n$, $n\le7$, mirroring Schoen–Simon stable-minimal-hypersurface theory; this would settle the stability interval.
- Determine the sharp dimension for the fractional and anisotropic Allen–Cahn analogues, where the relevant Bernstein theorem is unknown.

## 9. Key References

- **[Foundational]** E. De Giorgi. *Convergence problems for functionals and operators.* In *Proceedings of the International Meeting on Recent Methods in Nonlinear Analysis (Rome, 1978)*, Pitagora, Bologna, 1979, 131–188.
- **[Foundational]** E. Bombieri, E. De Giorgi, E. Giusti. *Minimal cones and the Bernstein problem.* Inventiones Mathematicae 7 (1969), 243–268.
- **[Foundational]** L. Modica. *A gradient bound and a Liouville theorem for nonlinear Poisson equations.* Communications on Pure and Applied Mathematics 38 (1985), 679–684.
- **[Foundational]** L. Modica. *The gradient theory of phase transitions and the minimal interface criterion.* Archive for Rational Mechanics and Analysis 98 (1987), 123–142.
- N. Ghoussoub, C. Gui. *On a conjecture of De Giorgi and some related problems.* Mathematische Annalen 311 (1998), 481–491.
- L. Ambrosio, X. Cabré. *Entire solutions of semilinear elliptic equations in $\mathbb{R}^3$ and a conjecture of De Giorgi.* Journal of the American Mathematical Society 13 (2000), 725–739.
- H. Berestycki, F. Hamel, R. Monneau. *One-dimensional symmetry of bounded entire solutions of some elliptic equations.* Duke Mathematical Journal 103 (2000), 375–396.
- D. Jerison, R. Monneau. *Towards a counter-example to a conjecture of De Giorgi in high dimensions.* Annali di Matematica Pura ed Applicata 183 (2004), 439–467.
- **[SOTA]** O. Savin. *Regularity of flat level sets in phase transitions.* Annals of Mathematics 169 (2009), 41–78.
- **[SOTA]** M. del Pino, M. Kowalczyk, J. Wei. *On De Giorgi's conjecture in dimension $N \ge 9$.* Annals of Mathematics 174 (2011), 1485–1569.
- F. Pacard, J. Wei. *Stable solutions of the Allen–Cahn equation in dimension 8 and minimal cones.* Journal of Functional Analysis 264 (2013), 1131–1167.
- Y. Liu, K. Wang, J. Wei. *Global minimizers of the Allen–Cahn equation in dimension $n \ge 8$.* Journal de Mathématiques Pures et Appliquées 108 (2017), 818–840.
- X. Cabré, J. Terra. *Saddle-shaped solutions of bistable diffusion equations in all of $\mathbb{R}^{2m}$.* Journal of the European Mathematical Society 11 (2009), 819–843.
- **[Survey]** A. Farina, E. Valdinoci. *The state of the art for a conjecture of De Giorgi and related problems.* In *Recent Progress on Reaction–Diffusion Systems and Viscosity Solutions*, World Scientific, 2009, 74–96.
- **[Survey]** H. Chan, J. Wei. *On De Giorgi's conjecture: recent progress and open problems.* Science China Mathematics 61 (2018), 1925–1946.

## 10. Worked Example / Concrete Special Case

**Step 1: the one-dimensional heteroclinic.** Seek $u(x) = g(x_n)$. Then $g'' = g^3 - g$. Multiply by $g'$ and integrate with $g(\pm\infty)=\pm1$, $g'(\pm\infty)=0$:
$$\tfrac12 (g')^2 = \tfrac14 (1-g^2)^2 \ \Longrightarrow\ g' = \tfrac{1}{\sqrt2}(1-g^2).$$
Separating, $\int \frac{dg}{1-g^2} = \frac{x_n}{\sqrt2} + c$, i.e. $\operatorname{artanh}(g) = \frac{x_n}{\sqrt2}+c$, so
$$g(t) = \tanh\!\Big(\tfrac{t}{\sqrt2}\Big),\qquad g' = \tfrac{1}{\sqrt2}\operatorname{sech}^2\!\Big(\tfrac{t}{\sqrt2}\Big) > 0 .$$
This is monotone, $|g|<1$, and its level sets are hyperplanes — the conjectured *only* behaviour.

**Step 2: surface tension.** With $t=\sqrt2 s$,
$$c_0 = \int_{\mathbb{R}}\Big(\tfrac12 (g')^2 + W(g)\Big)dt = \int_{\mathbb{R}} (g')^2 dt = \int_{\mathbb{R}} \tfrac12 \operatorname{sech}^4(s)\,\sqrt2\,ds = \tfrac{\sqrt2}{2}\cdot\tfrac43 = \tfrac{2\sqrt2}{3}.$$
Equality holds in Modica's bound $\tfrac12|\nabla u|^2 \le W(u)$ everywhere, as it must for 1D solutions.

**Step 3: why $n=9$ breaks it.** Let $\Gamma = \{x_9 = F(x_1,\dots,x_8)\} \subset \mathbb{R}^9$ be the Bombieri–De Giorgi–Giusti entire minimal graph, non-affine, with $F$ odd under $(x_1,\dots,x_4)\leftrightarrow(x_5,\dots,x_8)$ and $F$ growing like $|x|^{\alpha}$, $\alpha>1$, off the Simons cone. For small $\varepsilon>0$ set $\Gamma_\varepsilon = \varepsilon^{-1}\Gamma$ (still minimal, with curvature $O(\varepsilon)$) and take the ansatz
$$u_0(x) = \tanh\!\Big(\tfrac{\mathrm{dist}_{\pm}(x,\Gamma_\varepsilon)}{\sqrt2}\Big),$$
$\mathrm{dist}_\pm$ the signed distance, positive above the graph. Then $\Delta u_0 + u_0 - u_0^3 = O(\varepsilon^2)$ near $\Gamma_\varepsilon$, since the error is driven by the mean curvature $H_{\Gamma_\varepsilon} = 0$ plus quadratic curvature terms. Because $\Gamma_\varepsilon$ is a *graph* in the $x_9$ direction, $\mathrm{dist}_\pm$ is increasing in $x_9$, hence $\partial_{x_9} u_0 > 0$. Del Pino–Kowalczyk–Wei correct $u_0$ to an exact solution $u = u_0 + \phi$ by infinite-dimensional Lyapunov–Schmidt reduction, solving a Jacobi-field equation $\mathcal{J}_{\Gamma}h = $ error on $\Gamma$, and show monotonicity persists. Its zero level set is a small perturbation of $\Gamma_\varepsilon$ — not a hyperplane.

**Step 4: the dimension count.** The same recipe in $\mathbb{R}^n$, $n\le8$, needs a non-affine entire minimal graph over $\mathbb{R}^{n-1}$ with $n-1\le7$; Simons' theorem forbids one. That single inequality, $n-1 \le 7$, is the entire content of De Giorgi's "at least for $n \le 8$".

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*