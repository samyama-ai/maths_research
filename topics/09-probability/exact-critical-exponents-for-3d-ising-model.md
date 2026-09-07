---
id: 09-probability/exact-critical-exponents-for-3d-ising-model
title: "Exact Critical Exponents for 3D Ising Model"
topic: 09-probability
status: empirically-supported
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Exact Critical Exponents for the 3D Ising Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/exact-critical-exponents-for-3d-ising-model` · **Status:** empirically-supported

## 1. Problem Statement / Conjecture

Consider the nearest-neighbour ferromagnetic Ising model on $\mathbb{Z}^3$. The problem has three nested parts, none of which is resolved:

1. **Existence.** Prove that the critical exponents $\alpha,\beta,\gamma,\delta,\nu,\eta$ exist, i.e. that the relevant thermodynamic quantities are genuine power laws at $\beta_c$ (not merely bounded between powers).
2. **Identification.** Prove that the scaling limit at $\beta_c$ is conformally invariant and is described by a unique unitary 3D conformal field theory (CFT) with exactly two $\mathbb{Z}_2$-even and one $\mathbb{Z}_2$-odd relevant scalar operators — the hypothesis under which the numerical conformal bootstrap operates.
3. **Exactness.** Determine the exponents in closed form, or prove that no closed form of a specified type exists. In $d=2$ they are rational ($\beta=1/8$, $\eta=1/4$, $\nu=1$); in $d\ge 4$ they are mean-field. In $d=3$ the best values, $\nu = 0.629971(4)$ and $\eta = 0.0362978(20)$, match no known simple algebraic or hypergeometric expression.

A complete solution to (1)–(2) would be a theorem of probability theory; a solution to (3) would either exhibit an exact formula or establish a transcendence-type obstruction.

## 2. Mathematical Foundations

**Model.** On a finite $\Lambda \Subset \mathbb{Z}^3$ with $\sigma \in \{-1,+1\}^\Lambda$, the Hamiltonian and Gibbs measure are
$$H_\Lambda(\sigma) = -\sum_{\{x,y\}\subset\Lambda,\ |x-y|=1} \sigma_x\sigma_y - h\sum_{x\in\Lambda}\sigma_x, \qquad \mu_{\Lambda,\beta,h}(\sigma) = \frac{e^{-\beta H_\Lambda(\sigma)}}{Z_\Lambda(\beta,h)} .$$
By Griffiths' correlation inequalities the infinite-volume limits $\langle\cdot\rangle_\beta^+$ exist and are monotone. The critical point is
$$\beta_c = \inf\{\beta \ge 0 : m^*(\beta) := \langle \sigma_0\rangle^+_{\beta,h=0} > 0\},$$
numerically $\beta_c = 0.221\,654\,626(5)$ (Ferrenberg–Xu–Landau 2018).

**Exponents.** With $t = (\beta_c-\beta)/\beta_c$,
$$m^*(\beta) \sim |t|^{\beta_{\mathrm{ex}}}\ (t<0), \quad \chi(\beta)=\sum_{x}\langle\sigma_0\sigma_x\rangle^c \sim |t|^{-\gamma}, \quad \xi(\beta)\sim|t|^{-\nu},$$
$$\langle\sigma_0\sigma_x\rangle_{\beta_c} \sim |x|^{-(d-2+\eta)}, \quad m^*(\beta_c,h)\sim h^{1/\delta}, \quad c_V \sim |t|^{-\alpha}.$$

**Scaling and hyperscaling.** Assuming a single divergent length,
$$\alpha + 2\beta_{\mathrm{ex}} + \gamma = 2 \ \text{(Rushbrooke)}, \quad \gamma = \nu(2-\eta) \ \text{(Fisher)}, \quad \alpha = 2 - d\nu \ \text{(Josephson)},$$
so two independent exponents suffice. Rushbrooke and Fisher hold as *inequalities* ($\ge$) rigorously.

**CFT dictionary.** If the scaling limit is a unitary CFT, the exponents are scaling dimensions of the two lowest primaries $\sigma$ (odd) and $\epsilon$ (even):
$$\eta = 2\Delta_\sigma - d + 2, \qquad \nu = \frac{1}{d - \Delta_\epsilon}, \qquad \beta_{\mathrm{ex}} = \frac{\Delta_\sigma}{d-\Delta_\epsilon}, \qquad \delta = \frac{d-\Delta_\sigma}{\Delta_\sigma}.$$
Unitarity forces $\Delta_\sigma \ge (d-2)/2 = 1/2$, i.e. $\eta \ge 0$.

**Crossing equation.** The bootstrap constrains the four-point function $\langle\sigma\sigma\sigma\sigma\rangle$ through
$$\sum_{\mathcal{O}} \lambda_{\sigma\sigma\mathcal{O}}^2 \left[ v^{\Delta_\sigma} g_{\Delta,\ell}(u,v) - u^{\Delta_\sigma} g_{\Delta,\ell}(v,u) \right] = u^{\Delta_\sigma}-v^{\Delta_\sigma},$$
with $u,v$ the conformal cross-ratios and $g_{\Delta,\ell}$ conformal blocks. Positivity of $\lambda^2$ plus a linear functional gives rigorous exclusion regions in $(\Delta_\sigma,\Delta_\epsilon)$ — *conditional on the CFT hypothesis*.

## 3. History & State of the Art (SOTA)

- **1925** — Ising solves $d=1$ (no transition). **1936** — Peierls proves a transition for $d\ge 2$.
- **1944–1952** — Onsager computes the $d=2$ free energy; Yang derives $m^*=(1-\sinh^{-4}2\beta)^{1/8}$, giving $\beta_{\mathrm{ex}}=1/8$.
- **1972** — Wilson and Fisher introduce the $\varepsilon = 4-d$ expansion; $\nu = 1/2 + \varepsilon/12 + O(\varepsilon^2)$.
- **1982** — Aizenman and (independently) Fröhlich prove triviality of the scaling limit for $d>4$, hence mean-field exponents there.
- **1998–2002** — Field-theoretic resummations give $\nu = 0.6304(13)$ (Guida–Zinn-Justin); Pelissetto–Vicari survey consolidates.
- **2012–2016** — Numerical conformal bootstrap: El-Showk et al. isolate a "kink", then an island; Kos–Poland–Simmons-Duffin–Vichi obtain $\Delta_\sigma = 0.5181489(10)$, $\Delta_\epsilon = 1.412625(10)$, i.e. $\nu = 0.629971(4)$, $\eta = 0.0362978(20)$ — four orders of magnitude more precise than Monte Carlo at the time.
- **2018–2021** — Ferrenberg–Xu–Landau and Hasenbusch push Monte Carlo to $\nu = 0.62998(5)$, $\eta = 0.03631(3)$, in full agreement.
- **2021** — Aizenman–Duminil-Copin settle the marginal case $d=4$ (Annals of Mathematics): the scaling limit is Gaussian.

## 4. Partial Results / Verified Cases

| Regime | Status | Result |
|---|---|---|
| $d=1$ | Solved | No transition; $\beta_c=\infty$ |
| $d=2$ | Solved rigorously | $\beta_{\mathrm{ex}}=1/8$, $\eta=1/4$, $\nu=1$, $\gamma=7/4$, $\delta=15$; conformal invariance of the scaling limit proved (Chelkak–Smirnov 2012), magnetization field uniqueness (Camia–Garban–Newman 2015) |
| $d\ge 5$ | Solved rigorously | Mean-field: $\gamma=1$, $\beta_{\mathrm{ex}}=1/2$, $\delta=3$, $\nu=1/2$; $\eta=0$ for $d>4$ via the lace expansion (Sakai 2007) |
| $d=4$ | Solved rigorously | Marginal triviality; mean-field exponents with logarithmic corrections (Aizenman–Duminil-Copin 2021) |
| Infinite-range / spread-out $d>4$ | Solved | Same mean-field values |
| $d=3$, structural facts | Proved | Sharpness of the transition (Aizenman–Barsky–Fernández 1987; Duminil-Copin–Tassion 2016); continuity, $m^*(\beta_c)=0$ (Aizenman–Duminil-Copin–Sidoravicius 2015); exponential decay of truncated correlations for all $\beta\ne\beta_c$ (Duminil-Copin–Goswami–Raoufi 2020) |
| $d=3$, exponent bounds | Proved | $\gamma \ge 1$, $\delta\ge3$, $\nu\ge 1/2$ (mean-field bounds via random currents); $\eta\ge0$ conditionally on reflection positivity/CFT |
| $d=3$, exponent values | **Not proved** | Only numerics: bootstrap islands, MC, $\varepsilon$-expansion to six loops (Kompaniets–Panzer 2017) |

## 5. Principal Obstacles

- **No integrable structure.** The 2D solution rests on a free-fermion / transfer-matrix algebra (Onsager algebra, Yang–Baxter). The 3D transfer matrix generates no known commuting family; no star–triangle relation is available.
- **Correlation inequalities saturate at mean-field.** Random-current and Simon–Lieb inequalities are *one-sided*: they yield $\gamma\ge1$, $\delta\ge3$, and cannot produce the strict inequalities $\gamma > 1$ needed for non-classical behaviour, because the same inequalities are sharp for $d>4$.
- **Existence of the limit is itself open.** Power-law behaviour is not known: $\chi(\beta)$ could in principle oscillate logarithmically. Standard subadditivity arguments give bounds on $\liminf/\limsup$ of $\log\chi/\log|t|$ but no equality.
- **Conformal invariance unproved.** Even rotational invariance of the 3D critical scaling limit is open. Discrete holomorphicity, the engine of the 2D proofs, has no 3D analogue. Without conformal symmetry the crossing equation of Section 2 cannot be invoked, so bootstrap rigour is conditional.
- **$\varepsilon$-expansion is asymptotic.** The series in $\varepsilon = 4-d$ has zero radius of convergence with factorially growing, alternating coefficients; Borel summability of the $d=3$ series is not proved, and $\varepsilon=1$ is far from the perturbative regime.
- **Renormalization-group fixed points are non-constructive.** The Wilson–Fisher fixed point has been constructed rigorously only in hierarchical models and near $d=4$; no rigorous RG in $d=3$ controls the full lattice model.

## 6. The Gap

Proven: sharpness, continuity, mean-field *inequalities*, and the exact answers in $d=2$ and $d\ge4$. Conjectured but unproven: that the $d=3$ limits defining $\nu,\eta$ exist at all; that the limit theory is a rotation- and conformal-invariant unitary CFT with exactly the assumed relevant-operator spectrum; that this CFT is unique. The bootstrap island is a *rigorous consequence* of those assumptions plus numerical semidefinite programming with controlled error — so the gap is not numerical accuracy but the derivation of the CFT hypothesis from the lattice measure. A single missing step: **construct the scaling limit of the critical 3D Ising measure and prove it is conformally covariant.** Beyond that lies part (3): whether $\Delta_\epsilon = 1.412625\ldots$ is algebraic, and no technique currently addresses that question.

## 7. Current Research (as of June 2026)

- **Bootstrap precision.** Simmons-Duffin's group (Caltech) and collaborators use the "navigator" method and tiered SDPB runs on mixed correlators including the stress tensor; the 2024–2025 stress-tensor bootstrap reports $\Delta_\sigma$ and $\Delta_\epsilon$ with roughly an order of magnitude tighter error bars and a determination of the central charge $C_T$ *(frontier — verify)*.
- **Rigorous scaling limits.** Duminil-Copin (IHES/Geneva) and collaborators pursue random-current representations, the "OSSS" inequality, and near-critical percolation-style arguments aiming at rotational invariance in $d=3$; rotational invariance has been proved for critical planar random-cluster models but not in three dimensions.
- **Constructive RG.** Groups working on rigorous renormalization (Bauerschmidt, Brydges, Slade lineage) extend the $\varepsilon$-expansion rigorously in $4-\varepsilon$ dimensions for weakly self-avoiding walk and $\varphi^4$; extension to $\varepsilon=1$ remains out of reach.
- **Analytic bootstrap / fuzzy sphere.** Regularizing the 3D Ising CFT on a fuzzy two-sphere (Zhu, He and collaborators, 2022–2025) extracts operator dimensions and OPE coefficients from exact diagonalization of a Landau-level model; agreement at the $10^{-3}$ level *(frontier — verify)*.
- **Exactness questions.** Sporadic proposals for closed forms (e.g. relations to $\zeta$-values or to specific algebraic numbers) have all been excluded at current precision.

## 8. Future Work

- Prove existence of $\lim_{t\to0}\log\chi(t)/\log|t|$ — a weaker but still open target than computing $\gamma$.
- Establish rotational invariance of the critical 3D Ising scaling limit; this is widely seen as the decisive intermediate theorem, since conformal invariance would follow from rotational plus scale invariance under mild assumptions.
- Make the numerical bootstrap fully rigorous end to end: interval arithmetic in SDPB plus a proof that the lattice model's limit satisfies the CFT axioms would convert the islands into theorems.
- Prove Borel summability of the fixed-dimension $d=3$ perturbative series, which would give a rigorous (if imprecise) route to $\nu$.
- Settle whether $\Delta_\epsilon$ is irrational or transcendental; no framework exists, and constructing one is itself a research programme.

## 9. Key References

- **[Foundational]** L. Onsager. *Crystal Statistics I: A Two-Dimensional Model with an Order–Disorder Transition.* Physical Review 65, 117 (1944).
- **[Foundational]** C. N. Yang. *The Spontaneous Magnetization of a Two-Dimensional Ising Model.* Physical Review 85, 808 (1952).
- **[Foundational]** K. G. Wilson, M. E. Fisher. *Critical Exponents in 3.99 Dimensions.* Physical Review Letters 28, 240 (1972).
- **[Foundational]** M. Aizenman. *Geometric Analysis of $\varphi^4$ Fields and Ising Models.* Communications in Mathematical Physics 86, 1–48 (1982).
- **[Rigorous]** M. Aizenman, D. J. Barsky, R. Fernández. *The Phase Transition in a General Class of Ising-Type Models is Sharp.* Journal of Statistical Physics 47, 343–374 (1987).
- **[Rigorous]** M. Aizenman, H. Duminil-Copin, V. Sidoravicius. *Random Currents and Continuity of Ising Model's Spontaneous Magnetization.* Communications in Mathematical Physics 334, 719–742 (2015).
- **[Rigorous]** M. Aizenman, H. Duminil-Copin. *Marginal Triviality of the Scaling Limits of Critical 4D Ising and $\varphi_4^4$ Models.* Annals of Mathematics 194, 163–235 (2021).
- **[Rigorous]** A. Sakai. *Lace Expansion for the Ising Model.* Communications in Mathematical Physics 272, 283–344 (2007).
- **[Rigorous, 2D]** D. Chelkak, S. Smirnov. *Universality in the 2D Ising Model and Conformal Invariance of Fermionic Observables.* Inventiones Mathematicae 189, 515–580 (2012).
- **[Rigorous, 2D]** F. Camia, C. Garban, C. M. Newman. *Planar Ising Magnetization Field I. Uniqueness of the Critical Scaling Limit.* Annals of Probability 43, 528–571 (2015).
- **[SOTA]** S. El-Showk, M. F. Paulos, D. Poland, S. Rychkov, D. Simmons-Duffin, A. Vichi. *Solving the 3D Ising Model with the Conformal Bootstrap.* Physical Review D 86, 025022 (2012); and *…II. c-Minimization and Precise Critical Exponents.* Journal of Statistical Physics 157, 869–914 (2014).
- **[SOTA]** F. Kos, D. Poland, D. Simmons-Duffin, A. Vichi. *Precision Islands in the Ising and O(N) Models.* Journal of High Energy Physics 2016(08), 036.
- **[SOTA, numerics]** A. M. Ferrenberg, J. Xu, D. P. Landau. *Pushing the Limits of Monte Carlo Simulations for the Three-Dimensional Ising Model.* Physical Review E 97, 043301 (2018).
- **[SOTA, numerics]** M. Hasenbusch. *Restoring Isotropy in a Three-Dimensional Lattice Model: The Ising Universality Class.* Physical Review B 104, 014426 (2021).
- **[SOTA, perturbative]** M. V. Kompaniets, E. Panzer. *Minimally Subtracted Six-Loop Renormalization of O(n)-Symmetric $\varphi^4$ Theory and Critical Exponents.* Physical Review D 96, 036016 (2017).
- **[Survey]** A. Pelissetto, E. Vicari. *Critical Phenomena and Renormalization-Group Theory.* Physics Reports 368, 549–727 (2002).
- **[Survey]** D. Poland, S. Rychkov, A. Vichi. *The Conformal Bootstrap: Theory, Numerical Techniques, and Applications.* Reviews of Modern Physics 91, 015002 (2019).
- **[Survey]** H. Duminil-Copin. *Lectures on the Ising and Potts Models on the Hypercubic Lattice.* In *Random Graphs, Phase Transitions, and the Gaussian Free Field*, Springer PROMS 304, 35–161 (2020).

## 10. Worked Example / Concrete Special Case

**Deriving the full exponent set from two bootstrap numbers, and checking consistency.**

Input (Kos–Poland–Simmons-Duffin–Vichi 2016), $d=3$:
$$\Delta_\sigma = 0.5181489(10), \qquad \Delta_\epsilon = 1.412625(10).$$

Step 1 — anomalous dimension:
$$\eta = 2\Delta_\sigma - d + 2 = 2(0.5181489) - 1 = 0.0362978.$$

Step 2 — correlation length:
$$\nu = \frac{1}{d-\Delta_\epsilon} = \frac{1}{3-1.412625} = \frac{1}{1.587375} = 0.6299709.$$

Step 3 — remaining exponents by scaling:
$$\gamma = \nu(2-\eta) = 0.6299709 \times 1.9637022 = 1.237075,$$
$$\beta_{\mathrm{ex}} = \frac{\nu(d-2+\eta)}{2} = \frac{0.6299709 \times 1.0362978}{2} = 0.326419,$$
$$\delta = \frac{d+2-\eta}{d-2+\eta} = \frac{4.9637022}{1.0362978} = 4.78985,$$
$$\alpha = 2 - d\nu = 2 - 1.8899127 = 0.1100873.$$

Step 4 — Rushbrooke check:
$$\alpha + 2\beta_{\mathrm{ex}} + \gamma = 0.1100873 + 0.652838 + 1.237075 = 2.0000003,$$
consistent with $2$ to the propagated precision. Griffiths' rigorous result gives only $\alpha+2\beta_{\mathrm{ex}}+\gamma \ge 2$; equality is exactly the unproved hyperscaling assumption.

Step 5 — independent cross-check. Monte Carlo on lattices up to $L=1024$ gives $\nu = 0.62998(5)$ and $\eta = 0.03631(3)$; the two methods, sharing no assumptions beyond universality, agree to five digits.

**Contrast with dimensions where the answer is a theorem.** In $d=2$, $\Delta_\sigma = 1/8$ and $\Delta_\epsilon = 1$ give $\eta = 2(1/8) - 0 = 1/4$ and $\nu = 1/(2-1) = 1$ — both rational, both proved. In $d\ge5$, $\Delta_\sigma = (d-2)/2$ and $\Delta_\epsilon = 2$ give $\eta = 0$, $\nu = 1/2$ — proved by the lace expansion. In $d=3$ the same two-number recipe returns $0.0362978\ldots$ and $0.6299709\ldots$: numbers with no known closed form, obtained from a hypothesis that has not been derived from the lattice measure. That is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*