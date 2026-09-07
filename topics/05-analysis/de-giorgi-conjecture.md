---
id: 05-analysis/de-giorgi-conjecture
title: "De Giorgi Conjecture"
topic: 05-analysis
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# De Giorgi Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/de-giorgi-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $u \in C^2(\mathbb{R}^n)$ solve the Allen–Cahn equation

$$\Delta u + u - u^3 = 0 \quad \text{in } \mathbb{R}^n, \qquad |u| < 1,$$

and suppose $u$ is monotone in the last variable:

$$\partial_{x_n} u > 0 \quad \text{in } \mathbb{R}^n .$$

**Conjecture (De Giorgi, 1978).** If $n \le 8$, then $u$ is *one-dimensional*: there exist a unit vector $a \in S^{n-1}$ and $b \in \mathbb{R}$ with

$$u(x) = g(a \cdot x + b), \qquad g(t) = \tanh\!\left(\tfrac{t}{\sqrt 2}\right).$$

Equivalently, all level sets $\{u = \lambda\}$ are parallel hyperplanes.

De Giorgi stated it "at least for $n \le 8$", by analogy with the Bernstein problem for minimal graphs. A complete proof must handle every monotone bounded solution in dimensions $2$–$8$ with no extra hypothesis. A disproof requires an explicit monotone solution in some $n \le 8$ with non-planar level sets. The dimensional threshold is now known to be sharp: counterexamples exist for $n \ge 9$.

Two weaker variants are standard:

- **(BCN / weak form)** Assume additionally $\lim_{x_n \to \pm\infty} u(x', x_n) = \pm 1$ *pointwise* in $x'$.
- **(Gibbons / strong form)** Assume the limit is *uniform* in $x'$.
- **(Stable-solution form)** Drop monotonicity, assume only stability of $u$ as a critical point of the energy.

## 2. Mathematical Foundations

The equation is the Euler–Lagrange equation of the Allen–Cahn (Modica–Mortola) energy on bounded domains $\Omega \Subset \mathbb{R}^n$:

$$E_\Omega(u) = \int_\Omega \left( \tfrac12 |\nabla u|^2 + W(u) \right) dx, \qquad W(u) = \tfrac14 (1-u^2)^2 ,$$

with $\Delta u = W'(u) = u^3 - u$. The double-well potential $W \ge 0$ vanishes exactly at $u = \pm 1$.

**Stability.** $u$ is *stable* if the second variation is nonnegative:

$$Q_u(\varphi) = \int_{\mathbb{R}^n} \left( |\nabla \varphi|^2 + W''(u)\,\varphi^2 \right) dx \ge 0 \qquad \forall\, \varphi \in C_c^\infty(\mathbb{R}^n),$$

where $W''(u) = 3u^2 - 1$. Monotonicity implies stability: $\sigma := \partial_{x_n} u > 0$ satisfies the linearized equation $L\sigma := \Delta \sigma - W''(u)\sigma = 0$, and a positive solution of $L\sigma = 0$ gives $Q_u \ge 0$ by the substitution $\varphi = \sigma \psi$, which yields the **Picone/Sternberg–Zumbrun identity**

$$Q_u(\sigma\psi) = \int_{\mathbb{R}^n} \sigma^2 |\nabla \psi|^2 \, dx .$$

**Rescaled $\Gamma$-convergence.** Set $u_\varepsilon(x) = u(x/\varepsilon)$. Then $\varepsilon E(u_\varepsilon)$ $\Gamma$-converges (Modica, 1987) to $c_0 \operatorname{Per}(\{u=1\})$ with $c_0 = \int_{-1}^{1}\sqrt{2W(s)}\,ds = \tfrac{2\sqrt2}{3}$. Level sets of blow-downs therefore converge to minimal hypersurfaces, and a monotone $u$ has level sets that are graphs $\{x_n = \Gamma_\lambda(x')\}$.

**Modica's gradient bound.** For bounded entire solutions, $\tfrac12 |\nabla u|^2 \le W(u)$ on $\mathbb{R}^n$, with equality on a nonempty set forcing one-dimensionality.

**Bernstein connection.** Simons (1968) proved there are no stable minimal cones in $\mathbb{R}^n$, $n \le 7$, whence entire minimal graphs in $\mathbb{R}^{n}$, $n \le 8$, are affine. Bombieri–De Giorgi–Giusti (1969) constructed a nonplanar entire minimal graph over $\mathbb{R}^8$, asymptotic to the Simons cone $\{x_1^2+\dots+x_4^2 = x_5^2+\dots+x_8^2\}$. This dictates the exponent $8$ in the conjecture.

**Liouville lemma (Berestycki–Caffarelli–Nirenberg; Ghoussoub–Gui).** If $\sigma > 0$, $\operatorname{div}(\sigma^2 \nabla\psi) = 0$, and $\int_{B_R} (\sigma\psi)^2 \le C R^2$ for all $R$, then $\psi$ is constant. This is the engine of the low-dimensional proofs.

## 3. History & State of the Art (SOTA)

- **1978/79.** Ennio De Giorgi poses the conjecture at the Rome meeting *Recent Methods in Nonlinear Analysis*, framing it as the phase-transition analogue of Bernstein's theorem.
- **1980–1997.** Modica's gradient bound and equipartition results; Caffarelli–Garofalo–Segàla rigidity; Berestycki–Caffarelli–Nirenberg (1997) prove the $n=2$ case under the additional limit hypothesis and formulate the stable-solution variant.
- **1998.** Ghoussoub–Gui prove the full conjecture for $n = 2$ (no extra hypothesis), via the stability inequality plus the Liouville lemma.
- **2000.** Ambrosio–Cabré prove $n = 3$, using an energy-growth estimate $E_{B_R}(u) \le C R^{n-1}$ for monotone solutions.
- **2003.** Ghoussoub–Gui settle $n = 4, 5$ under an antisymmetry condition on two variables.
- **2009.** Savin proves $4 \le n \le 8$ under the pointwise limit hypothesis $u \to \pm 1$ as $x_n \to \pm\infty$, by an improvement-of-flatness theorem for level sets of minimizers.
- **2011.** del Pino–Kowalczyk–Wei construct a monotone solution in $\mathbb{R}^9$ whose zero set is a small perturbation of the BDG minimal graph — the conjecture is **false** for $n \ge 9$.
- **2017–2019.** Kelei Wang gives a new proof of Savin's theorem via a sharp minimal-surface-type estimate; Wang–Wei develop the finite-Morse-index theory.
- **2021–2025.** Chodosh–Li prove stable minimal hypersurfaces in $\mathbb{R}^4$ are flat; extensions to $\mathbb{R}^5$ (Chodosh–Li–Minter–Stryker) revive hope for the stable Allen–Cahn analogue in low dimensions.

## 4. Partial Results / Verified Cases

| Regime | Result | Reference |
|---|---|---|
| $n = 2$ | Full conjecture, no extra hypothesis | Ghoussoub–Gui 1998 |
| $n = 3$ | Full conjecture, no extra hypothesis | Ambrosio–Cabré 2000 |
| $n = 4, 5$ | Under antisymmetry in two variables | Ghoussoub–Gui 2003 |
| $4 \le n \le 8$ | Under pointwise limits $u \to \pm1$ | Savin 2009 (new proof: K. Wang 2017) |
| all $n$ | Under **uniform** limits (Gibbons conjecture) | Barlow–Bass–Gui 2000; Berestycki–Hamel–Monneau 2000; Farina 1999 |
| $n \le 4$, **stable** solutions | Rigidity for the stable variant; $n=4$ obtained from flatness of stable minimal hypersurfaces in $\mathbb{R}^4$ | Farina 1999 ($n\le3$ via Modica); Chodosh–Li 2021 *(frontier — verify for the full Allen–Cahn transfer)* |
| $n \le 10$, finite Morse index | Solutions have finitely many "ends"; level sets are asymptotically conical | Wang–Wei 2019 |
| $n \ge 9$ | **Counterexample**: monotone non-planar solution exists | del Pino–Kowalczyk–Wei 2011 |
| General $p$-Laplacian / fractional $(-\Delta)^s$ | Analogues proven in $n=2$ (all $s$), $n=3$ for $s \ge 1/2$ | Cabré–Cinti 2010, 2014; Cabré–Sire; Savin |

Also proven: any monotone solution in $\mathbb{R}^n$ with $n\le 8$ that is a *local minimizer* of the energy is one-dimensional (Savin), and any bounded solution with $E_{B_R}(u) \le CR^{n-1}$ and stable is one-dimensional in $n\le3$ (Farina).

## 5. Principal Obstacles

- **The missing limit hypothesis.** Savin's proof needs $u(x',x_n) \to \pm 1$ pointwise, which upgrades $u$ to a *local minimizer* of $E$ (via the sliding method and the fact that the limit profile is the 1D heteroclinic). Without it, a monotone solution is only known to be *stable*, and stability is strictly weaker than minimality for Allen–Cahn: the Simons-cone-type obstruction for stable, non-minimizing objects is only controlled up to dimension $3$ classically.
- **No Simons inequality for stable non-minimal phase transitions.** For minimal hypersurfaces, the Simons identity gives $\Delta_\Sigma |A|^2 \ge -|A|^4 + \tfrac{2}{n-1}|\nabla A|^2$, and combining with stability kills cones up to $n \le 7$. The diffuse-interface analogue loses the exact geometric curvature identity: level sets of $u$ are not minimal, only *almost* minimal at scale $1$, and the error terms are not sign-definite.
- **Failure of energy bounds.** Ambrosio–Cabré's $CR^{n-1}$ energy bound follows from monotonicity, but in $n \ge 4$ this bound alone does not force blow-downs to be *area-minimizing* — only stationary and stable. Classification of stable minimal cones is open for $6 \le n \le 7$ in the varifold class relevant here.
- **Sharpness at $n=9$ blocks soft arguments.** Any proof for $n \le 8$ must use dimension in an essential way; Fourier, Pohozaev, or moving-plane arguments that are dimension-agnostic cannot work, since they would contradict the DKW solution.
- **Multiplicity and interaction.** In the counterexample, the interface is a single BDG graph; near dimension $8$ the linearized Jacobi operator has slowly decaying kernel elements, so perturbative/gluing methods are delicate in both directions and give no contradiction argument at $n=8$.

## 6. The Gap

The precise open statement is:

> Let $n \in \{4,5,6,7,8\}$ and let $u$ solve $\Delta u + u - u^3 = 0$, $|u|<1$, $\partial_{x_n}u > 0$ on $\mathbb{R}^n$. **Without** assuming $\lim_{x_n\to\pm\infty} u = \pm 1$, is $u$ one-dimensional?

The gap is entirely the passage **stable $\Rightarrow$ minimizing** (or the direct classification of stable solutions). Monotonicity gives stability for free; the limit hypothesis gives minimality. If one could show that every monotone bounded solution in $\mathbb{R}^n$ automatically satisfies the pointwise limit condition — equivalently, that $\bar u(x') = \lim_{x_n\to\infty} u$ solves the equation in $\mathbb{R}^{n-1}$ and equals $1$ identically (this is known for $n\le 3$ by induction, since the limit is then a stable solution in dimension $n-1$) — Savin's theorem would close the conjecture. The induction breaks at $n=4$ because a stable solution in $\mathbb{R}^3$ with no monotonicity is only known to be 1D under a finite-energy-growth hypothesis, which the limit $\bar u$ inherits only partially.

## 7. Current Research (as of June 2026)

- **Stable Bernstein program.** Chodosh–Li (Stanford/Princeton) proved flatness of stable minimal hypersurfaces in $\mathbb{R}^4$; Chodosh–Li–Minter–Stryker announced $\mathbb{R}^5$ using stable-varifold sheeting and the Schoen–Yau $\mu$-bubble technique. Transferring these to the diffuse setting would yield De Giorgi in $n = 4, 5$ unconditionally. *(frontier — verify the diffuse transfer; the Allen–Cahn analogue requires uniform curvature estimates on level sets that are not yet established in $n=5$.)*
- **Kelei Wang (Wuhan)** and collaborators: quantitative sheet-separation and clustering estimates for stable Allen–Cahn solutions with unbounded energy.
- **Juncheng Wei (CUHK) and Manuel del Pino (Bath)**: refined gluing for higher-dimensional and vector-valued (Allen–Cahn system) analogues; classification of finite-Morse-index solutions.
- **Nonlocal versions.** Cabré, Cinti, Serra, Dipierro–Valdinoci: De Giorgi for $(-\Delta)^s u + u - u^3 = 0$; the case $n=4$, $s<1/2$ remains open. Cabré–Figalli–Ros-Oton–Serra's "stable solutions are smooth up to dimension 9" (Acta 2020) is being adapted to interior estimates for Allen–Cahn.
- **Numerics/computer-assisted.** Rigorous validated-numerics constructions of saddle-type solutions (Cabré–Terra saddle solutions in $\mathbb{R}^{2m}$, $2m \ge 8$) test whether monotone perturbations exist near $n=8$; no evidence of a counterexample below $9$.

## 8. Future Work

1. **Prove stable $\Rightarrow$ 1D in $\mathbb{R}^4$** for Allen–Cahn, mirroring Chodosh–Li. This is the most concrete next milestone and would also settle the Berestycki–Caffarelli–Nirenberg variant in $n=4$.
2. **Remove the limit hypothesis in Savin's theorem** by showing directly that the blow-down of a monotone solution is a minimizing cone, e.g. via a monotonicity formula tuned to the diffuse energy.
3. **Develop a diffuse Simons inequality**: a differential inequality for $|\nabla^2 u|$ along level sets with dimension-dependent constants matching $n \le 7$.
4. **Sharpen the counterexample side.** Understand whether the DKW construction admits any degeneration as $n \downarrow 8$; a quantitative obstruction at $n=8$ would explain the threshold structurally.
5. **Vector-valued and anisotropic analogues** (Allen–Cahn systems, anisotropic perimeters), where the Bernstein threshold itself is unknown.

## 9. Key References

- **[Foundational]** E. De Giorgi. *Convergence problems for functionals and operators.* Proceedings of the International Meeting on Recent Methods in Nonlinear Analysis (Rome, 1978), Pitagora, Bologna, 1979, 131–188.
- **[Foundational]** L. Modica. *A gradient bound and a Liouville theorem for nonlinear Poisson equations.* Communications on Pure and Applied Mathematics 38 (1985), 679–684.
- **[Foundational]** L. Modica. *The gradient theory of phase transitions and the minimal interface criterion.* Archive for Rational Mechanics and Analysis 98 (1987), 123–142.
- **[Foundational]** E. Bombieri, E. De Giorgi, E. Giusti. *Minimal cones and the Bernstein problem.* Inventiones Mathematicae 7 (1969), 243–268.
- **[Foundational]** J. Simons. *Minimal varieties in riemannian manifolds.* Annals of Mathematics 88 (1968), 62–105.
- **[Key case]** H. Berestycki, L. Caffarelli, L. Nirenberg. *Further qualitative properties for elliptic equations in unbounded domains.* Annali della Scuola Normale Superiore di Pisa, Cl. Sci. 25 (1997), 69–94.
- **[Key case]** N. Ghoussoub, C. Gui. *On a conjecture of De Giorgi and some related problems.* Mathematische Annalen 311 (1998), 481–491.
- **[Key case]** L. Ambrosio, X. Cabré. *Entire solutions of semilinear elliptic equations in $\mathbb{R}^3$ and a conjecture of De Giorgi.* Journal of the American Mathematical Society 13 (2000), 725–739.
- **[Key case]** N. Ghoussoub, C. Gui. *On De Giorgi's conjecture in dimensions 4 and 5.* Annals of Mathematics 157 (2003), 313–334.
- **[SOTA]** O. Savin. *Regularity of flat level sets in phase transitions.* Annals of Mathematics 169 (2009), 41–78.
- **[SOTA]** M. del Pino, M. Kowalczyk, J. Wei. *On De Giorgi's conjecture in dimension $N \ge 9$.* Annals of Mathematics 174 (2011), 1485–1569.
- **[SOTA]** K. Wang. *A new proof of Savin's theorem on Allen–Cahn equations.* Journal of the European Mathematical Society 19 (2017), 2997–3051.
- **[SOTA]** K. Wang, J. Wei. *Finite Morse index implies finite ends.* Communications on Pure and Applied Mathematics 72 (2019), 1044–1119.
- **[SOTA]** X. Cabré, A. Figalli, X. Ros-Oton, J. Serra. *Stable solutions to semilinear elliptic equations are smooth up to dimension 9.* Acta Mathematica 224 (2020), 187–252.
- **[SOTA]** O. Chodosh, C. Li. *Stable minimal hypersurfaces in $\mathbb{R}^4$.* arXiv:2108.11462, 2021.
- **[Survey]** H. Chan, J. Wei. *On De Giorgi's conjecture: recent progress and open problems.* Science China Mathematics 61 (2018), 1925–1946.
- **[Survey]** A. Farina, E. Valdinoci. *The state of the art for a conjecture of De Giorgi and related problems.* In *Recent Progress on Reaction-Diffusion Systems and Viscosity Solutions*, World Scientific, 2009, 74–96.

## 10. Worked Example / Concrete Special Case

**Step 1 — the one-dimensional profile.** Take $g(t) = \tanh(t/\sqrt2)$. Then $g'(t) = \tfrac{1}{\sqrt2}\operatorname{sech}^2(t/\sqrt2)$ and

$$g''(t) = -\operatorname{sech}^2\!\left(\tfrac{t}{\sqrt2}\right)\tanh\!\left(\tfrac{t}{\sqrt2}\right) = -(1-g^2)g = g^3 - g,$$

so $g'' + g - g^3 = 0$. Equipartition holds exactly:

$$\tfrac12 (g')^2 = \tfrac14 \operatorname{sech}^4\!\left(\tfrac{t}{\sqrt2}\right) = \tfrac14 (1-g^2)^2 = W(g),$$

i.e. Modica's inequality is an equality. The transition energy is

$$\int_{\mathbb{R}} \left(\tfrac12 (g')^2 + W(g)\right) dt = \tfrac{1}{2}\int_{\mathbb{R}} \operatorname{sech}^4\!\left(\tfrac{t}{\sqrt2}\right) dt = \tfrac{\sqrt2}{2}\cdot\tfrac43 = \tfrac{2\sqrt2}{3} = c_0 .$$

For any $a\in S^{n-1}$ with $a_n>0$, $u(x)=g(a\cdot x + b)$ is an entire solution with $\partial_{x_n}u = a_n g' > 0$. The conjecture asserts these are all of them for $n \le 8$.

**Step 2 — why $n=2$ closes.** Let $u$ be monotone on $\mathbb{R}^2$, $\sigma = \partial_{x_2}u > 0$, and set $\psi = \partial_{x_1}u/\sigma$. Differentiating the equation gives $L(\partial_{x_1}u) = L\sigma = 0$, hence

$$\operatorname{div}(\sigma^2 \nabla \psi) = \sigma L(\partial_{x_1} u) - (\partial_{x_1} u) L\sigma = 0 .$$

Modica's bound gives $|\nabla u| \le \sqrt{2W(u)} \le \tfrac{1}{\sqrt2}$, so $\int_{B_R}(\sigma\psi)^2 = \int_{B_R}|\partial_{x_1}u|^2 \le \tfrac12 |B_R| = O(R^2)$. The Liouville lemma applies: $\psi \equiv c$, so $\partial_{x_1}u = c\,\partial_{x_2}u$, meaning $\nabla u$ is everywhere parallel to the fixed vector $a = (c,1)/\sqrt{1+c^2}$. Hence $u = g(a\cdot x + b)$.

**Step 3 — where it breaks at $n=4$.** The same computation in $\mathbb{R}^n$ gives $\int_{B_R} |\partial_{x_1}u|^2 = O(R^n)$, but the Liouville lemma needs $O(R^2)$. Ambrosio–Cabré recover $O(R^{n-1})$ from the monotone energy bound, enough only for $n=3$. For $n \ge 4$ one must instead classify blow-downs, and that is exactly where minimality — not just stability — is required.

**Step 4 — the $n = 9$ counterexample in one line.** Let $F:\mathbb{R}^8 \to \mathbb{R}$ be the BDG entire minimal graph asymptotic to the Simons cone. del Pino–Kowalczyk–Wei build $u_\varepsilon(x) \approx g\!\left(\tfrac{x_9 - \varepsilon^{-1}F(\varepsilon x')}{\text{(normal distance)}}\right)$, correcting by an infinite-dimensional Lyapunov–Schmidt reduction whose reduced equation is the Jacobi equation on the BDG graph. The result is monotone in $x_9$ with non-planar level sets — dimension $9$ is where the geometry first permits it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*