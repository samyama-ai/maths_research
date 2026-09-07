---
id: 06-pdes/landis-conjecture-exponential-decay
title: "Landis Conjecture on Exponential Decay"
topic: 06-pdes
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Landis Conjecture on Exponential Decay

> **Topic:** Partial Differential Equations · **ID:** `06-pdes/landis-conjecture-exponential-decay` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $u : \mathbb{R}^n \to \mathbb{R}$ be a solution of the stationary Schrödinger equation
$$\Delta u - V u = 0 \quad \text{in } \mathbb{R}^n,$$
with a measurable potential satisfying $\|V\|_{L^\infty(\mathbb{R}^n)} \le 1$, and suppose $u$ is bounded, $\|u\|_{L^\infty} \le C_0$.

**Landis conjecture.** If
$$|u(x)| \le C\,\exp\!\big(-c\,|x|^{1+\varepsilon}\big) \quad \text{for some } \varepsilon > 0,\ c>0,$$
then $u \equiv 0$.

Equivalently: a nontrivial bounded solution cannot decay faster than any exponential $e^{-c|x|}$; the exponential rate $|x|^1$ dictated by $\|V\|_\infty \le 1$ is the true barrier. A proof must produce this quantitative unique-continuation-at-infinity statement for all bounded real $V$ in all dimensions; a disproof must exhibit a real bounded $V$ and a nontrivial bounded $u$ with super-exponential decay.

Two refinements are tracked separately:

- **(Sharp form)** $|u(x)| \le C e^{-c|x|}$ with $c$ large enough (depending on $n$) already forces $u \equiv 0$.
- **(Complex form)** The same statement for complex-valued $u$ and $V$. This version is **false** (Meshkov, 1992).

## 2. Mathematical Foundations

**Operator and normalization.** Write $L u = \Delta u - Vu$, $V \in L^\infty(\mathbb{R}^n;\mathbb{R})$. Scaling $u_\lambda(x)=u(\lambda x)$ gives $\Delta u_\lambda = \lambda^2 V(\lambda x) u_\lambda$, so $\|V\|_\infty \le 1$ is a normalization, not a restriction: it fixes the length scale at which the potential is felt.

**Order of vanishing at infinity.** For $R>0$ set
$$m(R) := \inf_{|x_0| = R} \ \sup_{|x-x_0| \le 1} |u(x)| .$$
Landis' question is the largest $\beta$ for which $m(R) \gtrsim e^{-CR^{\beta}}$ must hold for nontrivial $u$. The conjecture asserts $\beta = 1$; Meshkov's theorem gives $\beta = 4/3$ in the complex case, and this is sharp there.

**Carleman estimates.** The workhorse is a weighted inequality of the form
$$\tau^{3}\!\int e^{2\tau \phi} |w|^2 \,dx \ \le\ C \int e^{2\tau \phi} |\Delta w|^2 dx , \qquad w \in C_c^\infty(\Omega\setminus\{0\}),$$
with $\phi$ a suitable (pseudo)convex weight, e.g. $\phi = -\log|x| + $ correction, or $\phi(x) = e^{\sigma|x|}$. Absorbing $Vw$ requires $\tau^{3} \gg \|V\|_\infty^2$, i.e. $\tau \gtrsim \|V\|_\infty^{2/3}$. After rescaling an annulus of radius $R$ to unit size the effective potential has size $R^2$, so $\tau \sim R^{4/3}$ — this is the analytic origin of the exponent $4/3$ and the reason Carleman methods alone stop exactly at Meshkov's rate.

**Three-ball / doubling formulation.** Landis' conjecture is equivalent to a quantitative three-ball inequality with linear-in-$R$ loss: for $|x_0| = R$,
$$\sup_{B_1(x_0)} |u| \ \ge\ e^{-CR}\ \sup_{B_1(0)} |u| .$$
The frequency function $N(r) = r\int_{B_r}|\nabla u|^2 / \int_{\partial B_r} u^2$ and its almost-monotonicity give doubling indices; controlling $N$ on scale-$R$ balls by $O(R)$ rather than $O(R^{4/3})$ is exactly the conjecture.

**Positive-solution mechanism.** If $V \ge 0$, then $\Delta u = Vu$ admits a positive supersolution comparison; the Vázquez strong maximum principle and Harnack chains convert the sign condition into a linear-rate bound, which is why the $V \ge 0$ case is far more accessible.

## 3. History & State of the Art (SOTA)

- **1960s.** E. M. Landis poses the question in his work on qualitative properties of second-order elliptic equations; it is recorded in the survey monograph of V. A. Kondratiev and E. M. Landis (1988).
- **1992.** V. Z. Meshkov constructs complex-valued $V, u$ on $\mathbb{R}^2$ with $\|V\|_\infty \le 1$, $u \not\equiv 0$, and $|u(x)| \le C\exp(-c|x|^{4/3})$, disproving the complex version; he proves the matching positive result that decay $e^{-c|x|^{4/3+\varepsilon}}$ forces $u \equiv 0$. The exponent $4/3$ is sharp for complex data.
- **2005.** J. Bourgain and C. Kenig give a quantitative $L^\infty$ version of Meshkov's bound, $\sup_{B_1(x_0)}|u| \gtrsim e^{-C|x_0|^{4/3}\log|x_0|}$, used to prove Anderson localization for the continuous Bernoulli model. This made the $4/3$ exponent a central object in spectral theory.
- **2005 onward.** Kenig repeatedly highlights the real case as open, including in his ICM-adjacent surveys; the problem becomes a benchmark for unique continuation at infinity.
- **2015.** Kenig, Silvestre and Wang prove the plane case for real $V \ge 0$, including a drift term.
- **2017–2021.** Davey, Kenig, Wang extend to variable-coefficient operators and to potentials with growth or decay; Rossi obtains sharp-rate versions under sign conditions in all dimensions; Sirakov and Souplet treat unbounded coefficients via maximum-principle methods.
- **2020–2021.** Logunov, Malinnikova, Nadirashvili and Nazarov settle the real planar case with no sign assumption, in a form *stronger* than Landis conjectured.

State of the art: **true in $n=2$ for real $V$; false for complex $V$; open for real $V$ in every dimension $n \ge 3$.**

## 4. Partial Results / Verified Cases

- **Dimension $n = 2$, real $V$, $\|V\|_\infty \le 1$ (Logunov–Malinnikova–Nadirashvili–Nazarov, 2020).** If $u$ is a real bounded solution of $\Delta u = Vu$ in $\mathbb{R}^2$ with
  $$|u(x)| \le \exp\big(-C|x|\log|x|\big)$$
  for large $C$, then $u \equiv 0$. Since $|x|\log|x| = o(|x|^{1+\varepsilon})$, this implies the Landis conjecture in the plane and leaves only a logarithmic gap to the sharp rate $e^{-c|x|}$. The proof uses quasiconformal maps and the geometry of nodal sets of real solutions in 2D.
- **$V \ge 0$, plane, with drift (Kenig–Silvestre–Wang, 2015).** For $\Delta u - \nabla \cdot (W u) - Vu = 0$ in $\mathbb{R}^2$ with $V \ge 0$, $\|V\|_\infty, \|W\|_\infty \le 1$, decay $|u| \le e^{-c|x|^{1+}}$ forces $u\equiv0$; quantitatively $\sup_{B_1(x_0)}|u| \ge e^{-C|x_0|\log|x_0|}$.
- **Sign-definite potentials in all dimensions.** Rossi (2021) proves the conjecture with the *sharp* rate $e^{-c|x|}$ for real potentials obeying a sign/structure condition (notably $V \ge 0$ bounded away from $0$ at infinity), in arbitrary $n$, by maximum-principle and generalized-principal-eigenvalue arguments rather than Carleman estimates. Sirakov–Souplet (2021) extend such results to unbounded drift and zeroth-order coefficients.
- **Variable coefficients.** Davey–Kenig–Wang (2017) prove planar Landis-type theorems for $\operatorname{div}(A\nabla u) - Vu = 0$ with Lipschitz uniformly elliptic $A$.
- **Decaying/growing potentials.** For $|V(x)| \lesssim (1+|x|)^{-\delta}$, Davey and collaborators obtain the expected rate $e^{-c|x|^{1-\delta/2}}$ interpolating between $4/3$ and $1$; for $|V| \lesssim |x|^{M}$ the corresponding $\frac{4}{3}$-type exponent $\frac{M+2}{3}\!+\!\ldots$ bounds are established.
- **Complex case, sharp.** Meshkov: decay $e^{-c|x|^{4/3+\varepsilon}}$ forces $u\equiv0$; $4/3$ cannot be improved.

## 5. Principal Obstacles

- **Carleman estimates are dimension- and field-blind.** Every Carleman weight known for $\Delta - V$ uses only $\|V\|_\infty$; the derivation never sees whether $V$ and $u$ are real. Since Meshkov's counterexample saturates $4/3$ for complex data, *any* argument that works verbatim for complex-valued solutions cannot reach exponent $1$. Improving Landis requires a genuinely real-variable input.
- **The 2D proof is conformal.** The LMNN argument uses that a real solution in the plane has a nodal set which, after a quasiconformal change of variables, behaves like the zero set of a harmonic function; $u$ can be paired with a conjugate-type object. Neither quasiconformal machinery nor the Beltrami equation has a substitute in $n \ge 3$.
- **Nodal geometry degenerates.** In 2D, nodal sets are curves and doubling indices are controlled by counting nodal domains crossing an annulus. In $n \ge 3$ nodal sets are hypersurfaces of unbounded complexity; no counting principle converts nodal structure into a linear-in-$R$ frequency bound.
- **Frequency functions lose too much.** Almost-monotonicity of $N(r)$ under a bounded potential yields $N(R) \lesssim R^{4/3}$ only, matching Carleman. There is no known monotonicity formula sensitive to the reality of $V$.
- **Oscillation is the enemy.** Meshkov's construction decays by inserting rapidly rotating phases $e^{i\varphi}$ on successive annuli: a complex solution can "spend" oscillation to buy extra decay. Real solutions cannot rotate phase, but no analytic quantity in $n\ge3$ currently measures this deficit.

## 6. The Gap

Proven: exponent $1$ (indeed $|x|\log|x|$) for **real** $V$ in **dimension 2**; exponent $4/3$ for all $n$ and all bounded complex $V$; exponent $1$ in all $n$ for **sign-definite** real $V$.

Conjectured: exponent $1$ for arbitrary real bounded $V$ in $n \ge 3$.

The precise missing step: a quantitative unique-continuation estimate
$$\sup_{B_1(x_0)} |u| \ \ge\ \exp\big(-C|x_0|\,\log|x_0|\big), \qquad n \ge 3,\ V \text{ real},$$
that improves the universal $4/3$-power bound using only reality of $u$ and $V$. Concretely, one needs a Carleman weight, frequency function, or geometric-measure argument whose constants degrade when $u$ is forced to change sign — i.e. a mechanism that fails for $e^{i\varphi}$-type solutions. A secondary gap is the logarithm: closing $e^{-C|x|\log|x|}$ to the sharp $e^{-c|x|}$, open even in the plane for sign-changing $V$.

## 7. Current Research (as of June 2026)

- **Extending LMNN beyond the plane.** Groups around Logunov (Princeton/Geneva), Malinnikova (Stanford), and Nazarov (St. Petersburg / Michigan State) are probing whether nodal-set techniques from the Yau/Nadirashvili circle — combination of doubling-index simplex decompositions and harmonic-measure estimates — can substitute for quasiconformality in $n = 3$. No unconditional result yet. *(frontier — verify)*
- **Maximum-principle route.** Following Rossi and Sirakov–Souplet, work continues on generalized principal eigenvalues and Vázquez-type strong maximum principles to widen the class of real $V$ (e.g. $V \ge 0$ only outside a compact set, or $V^-$ small in a scale-invariant norm) in arbitrary dimension.
- **Quantitative/spectral applications.** Bourgain–Kenig-style bounds continue to drive Anderson-localization results; a real-Landis improvement in $n \ge 3$ would directly sharpen localization length estimates for real random potentials. Active at Kenig's school (Chicago) and among mathematical physicists working on Bernoulli–Anderson models. *(frontier — verify)*
- **Fractional and nonlocal analogues.** Landis-type decay questions for $(-\Delta)^s u = Vu$ are studied via Caffarelli–Silvestre extension; the correct exponent is not settled.
- **Systems and Dirac operators.** Meshkov-type counterexamples generalize to systems; identifying the algebraic structure responsible for $4/3$ (essentially the two real components of a complex solution) is a live line of inquiry.

## 8. Future Work

- Find an invariant that vanishes for real solutions and is large for phase-rotating complex ones — a "reality defect" entering Carleman constants.
- Develop a higher-dimensional analogue of the LMNN quasiconformal comparison, e.g. via $A$-harmonic functions or quasiregular mappings in $\mathbb{R}^n$.
- Remove the $\log$ from the planar bound to obtain the sharp exponential rate $e^{-c|x|}$ for sign-changing $V$.
- Classify all real $V$ for which the sharp rate holds in $n\ge3$ (sign conditions, radial symmetry, small $V^-$).
- Construct real counterexamples in high dimension, or prove a rigidity theorem showing none exists — even a real example with exponent $1+\varepsilon$ for some small $\varepsilon$ would reorient the field.
- Settle the nonlocal and variable-coefficient versions, where the expected exponents are conjectural.

## 9. Key References

- **[Foundational]** V. A. Kondratiev and E. M. Landis. *Qualitative theory of second order linear partial differential equations.* In: Partial Differential Equations III, Encyclopaedia of Mathematical Sciences, Springer, 1988.
- **[Foundational]** V. Z. Meshkov. *On the possible rate of decrease at infinity of the solutions of second-order partial differential equations.* Mathematics of the USSR-Sbornik, Vol. 72, No. 2, 1992, pp. 343–361.
- **[Foundational]** J. Bourgain and C. E. Kenig. *On localization in the continuous Anderson–Bernoulli model in higher dimension.* Inventiones Mathematicae, Vol. 161, 2005, pp. 389–426.
- **[SOTA / Recent]** A. Logunov, E. Malinnikova, N. Nadirashvili and F. Nazarov. *The Landis conjecture on exponential decay.* arXiv:2007.07034, 2020.
- **[SOTA / Recent]** C. Kenig, L. Silvestre and J.-N. Wang. *On Landis' conjecture in the plane.* Communications in Partial Differential Equations, Vol. 40, No. 4, 2015, pp. 766–789.
- **[SOTA / Recent]** B. Davey, C. Kenig and J.-N. Wang. *The Landis conjecture for variable coefficient second-order elliptic PDEs.* Transactions of the American Mathematical Society, Vol. 369, 2017, pp. 8209–8237.
- **[SOTA / Recent]** L. Rossi. *The Landis conjecture with sharp rate of decay.* Indiana University Mathematics Journal, Vol. 70, No. 1, 2021, pp. 301–324.
- **[SOTA / Recent]** B. Sirakov and P. Souplet. *The Vázquez maximum principle and the Landis conjecture for elliptic PDE with unbounded coefficients.* Advances in Mathematics, Vol. 387, 2021, 107838.
- **[Survey]** C. E. Kenig. *Some recent applications of unique continuation.* Contemporary Mathematics, Vol. 439, American Mathematical Society, 2007, pp. 25–56.
- **[Survey]** B. Davey. *Quantitative uniqueness for elliptic equations and Landis-type theorems.* (Expository work on decay estimates for Schrödinger operators; see also Davey, *On Landis' conjecture in the plane when the potential has an exponentially decaying negative part*, St. Petersburg Mathematical Journal, Vol. 31, 2020.)

## 10. Worked Example / Concrete Special Case

**Claim.** The exponent $1$ in Section 1 cannot be lowered: there is a real bounded $V$ with $\|V\|_\infty \le n+1$ and a nontrivial bounded solution decaying exactly like $e^{-|x|}$.

Take on $\mathbb{R}^n$
$$u(x) = e^{-\rho(x)}, \qquad \rho(x) = \sqrt{1 + |x|^2}\ \ (\text{smooth, } \rho \ge 1).$$

Write $r = |x|$. Then $\partial_i \rho = x_i/\rho$, so $|\nabla \rho|^2 = r^2/\rho^2$ and
$$\Delta \rho = \frac{n}{\rho} - \frac{r^2}{\rho^3}.$$
Since $\Delta e^{-\rho} = e^{-\rho}\big(|\nabla\rho|^2 - \Delta\rho\big)$,
$$\Delta u = u\left(\frac{r^2}{\rho^2} - \frac{n}{\rho} + \frac{r^2}{\rho^3}\right) =: V u .$$
Hence $u$ solves $\Delta u - Vu = 0$ with $V$ real, smooth, and
$$|V(x)| \le \frac{r^2}{\rho^2} + \frac{n}{\rho} + \frac{r^2}{\rho^3} \le 1 + n + 1 = n+2,$$
while $V(x) \to 1$ as $|x| \to \infty$. Rescaling $\tilde u(x) = u(\lambda x)$ with $\lambda = (n+2)^{-1/2}$ normalizes $\|\tilde V\|_\infty \le 1$ at the cost of replacing the decay by $e^{-\lambda|x|}$.

**Reading.** $u$ is bounded, nontrivial, and $|u(x)| = e^{-|x|}(1+O(|x|^{-1}))$ — decay of exact order $e^{-c|x|}$. So no theorem can force $u \equiv 0$ from decay $e^{-c|x|}$ alone with $c$ small; the conjecture asserts that the *only* room left is the constant $c$, and that any strictly super-exponential decay $e^{-c|x|^{1+\varepsilon}}$ is impossible.

**Contrast with Meshkov.** In $\mathbb{R}^2$ Meshkov builds $u = f e^{i\varphi}$ where on each dyadic annulus $|x| \sim R_k$ the phase $\varphi$ winds $\sim R_k^{1/3}$ times. Solving $\Delta u = Vu$ for $V$ then costs $|V| \lesssim 1$, while the amplitude $f$ can be driven down by a factor $\exp(-c R_k^{1/3} \cdot R_k) = \exp(-cR_k^{4/3})$ across the annulus. Iterating over $k$ gives $|u(x)| \le e^{-c|x|^{4/3}}$. The construction is impossible for real $u$: a real solution has no phase to wind, and it is exactly this missing degree of freedom — quantified in dimension $2$ by LMNN, unquantified in dimension $\ge 3$ — that separates the theorem from the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*