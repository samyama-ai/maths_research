---
id: 09-probability/forest-fire-model-critical-exponents
title: "Critical Exponents for the Self-Organized Forest Fire Model"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Critical Exponents for the Self-Organized Forest Fire Model

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/forest-fire-model-critical-exponents` · **Status:** open

## 1. Problem Statement / Conjecture

The Drossel–Schwabl (DS) forest fire model on $\mathbb{Z}^d$ is an interacting particle system with two rates: trees grow at rate $1$ on vacant sites, and lightning strikes each site at rate $\lambda > 0$, instantly destroying the entire occupied cluster containing the struck site. The model is *self-organized critical* (SOC) in the sense that, as $\lambda \downarrow 0$, the stationary state is believed to approach a scale-invariant state without tuning any parameter to a critical value.

**The problem.** Prove that as $\lambda \downarrow 0$ the two-dimensional stationary DS model has a genuine scaling limit, and identify the associated critical exponents. Concretely, prove or disprove that there exist constants $\tau, \nu, D$ such that the stationary cluster-size distribution obeys
$$ P_\lambda(|C| = s) \;\asymp\; s^{-\tau}\, \Phi\!\left(s/s_{\max}(\lambda)\right), \qquad s_{\max}(\lambda) \asymp \lambda^{-\lambda_{\mathrm{cut}}}, \qquad \xi(\lambda) \asymp \lambda^{-\nu}, $$
with $s_{\max} \asymp \xi^{D}$, and determine the numerical values of $\tau$, $\nu$, $D$. A complete solution must either (i) establish existence of the limits defining the exponents together with their values, or (ii) show that no such power laws exist — that the apparent exponents drift with $\lambda$ and the model is not critical in the scaling-limit sense.

The negative alternative is live: the strongest rigorous two-dimensional result to date (Kiss–Manolescu–Sidoravicius) shows that the near-critical structure produced by fires does *not* relax back to critical percolation, which is exactly the assumption underlying the physicists' exponent predictions.

## 2. Mathematical Foundations

**State space and generator.** Configurations are $\eta \in \{0,1\}^{\mathbb{Z}^d}$, $\eta(x)=1$ meaning "occupied by a tree". For $x \in \mathbb{Z}^d$ let $C(x,\eta)$ be the connected component of $x$ in $\{y : \eta(y)=1\}$ (nearest-neighbour connectivity), with $C(x,\eta)=\emptyset$ if $\eta(x)=0$. The formal generator is
$$ (\mathcal{L}f)(\eta) \;=\; \sum_{x} \mathbf{1}_{\{\eta(x)=0\}}\big[f(\eta^{x\to 1}) - f(\eta)\big] \;+\; \lambda \sum_x \mathbf{1}_{\{\eta(x)=1\}}\big[f(\eta^{C(x,\eta)\to 0}) - f(\eta)\big], $$
where $\eta^{C \to 0}$ sets all of $C$ to $0$. In infinite volume this is not a standard Liggett-type generator: the fire map $\eta \mapsto \eta^{C\to 0}$ is not a local function, and when the tree density exceeds $p_c$ an infinite cluster would have to burn instantaneously.

**Existence.** Dürre (2006) constructed the process on $\mathbb{Z}^d$, $d \ge 2$, for every $\lambda>0$, using the *no-infinite-cluster* convention (only finite clusters burn) and a graphical/percolation argument controlling the range of dependence; he also proved uniqueness in a subsequent paper. In $d=1$ existence is elementary. The stationary measure $\mu_\lambda$ (obtained as a subsequential limit of the process started from the empty configuration) is the object of interest.

**Steady-state balance.** In the stationary state, the density of trees $\rho(\lambda)$ satisfies growth = burning:
$$ 1-\rho(\lambda) \;=\; \lambda \,\mathbb{E}_{\mu_\lambda}\!\big[\,|C(0)|\,\big] \;\Longrightarrow\; \mathbb{E}_{\mu_\lambda}|C(0)| \;\asymp\; \theta := \lambda^{-1} \quad \text{if } \rho \to \rho_\infty < 1. $$
This is the one *exact* constraint on the exponents. Writing $P_\lambda(|C(0)| = s) \sim s^{1-\tau}$ for the size-biased (site-sampled) distribution truncated at $s_{\max}$, the constraint $\mathbb{E}|C(0)| \asymp \lambda^{-1}$ forces, for $2 < \tau < 3$,
$$ s_{\max}^{\,3-\tau} \asymp \lambda^{-1} \quad \Longrightarrow \quad \boxed{\;\lambda_{\mathrm{cut}}\,(3-\tau) = 1\;} \qquad\text{and}\qquad \lambda_{\mathrm{cut}} = \nu D . $$

**Percolation input.** The heuristic derivation of $\nu$ assumes that a region which has just burned regrows as (near-)critical Bernoulli percolation, so that standard 2D critical exponents apply: $D = 91/48$ (fractal dimension of the incipient infinite cluster), $\tau_{\mathrm{perc}} = 1 + d/D = 187/91$, correlation-length exponent $4/3$. The conjecture $\tau_{\mathrm{DS}} = 187/91 \approx 2.055$ is *rejected* by simulation, which is the crux of the problem.

**Related exactly solvable relatives.** Frozen percolation (Aldous 1999) on the binary tree; volume-frozen percolation on $\mathbb{Z}^2$ (van den Berg–de Lima–Nolin); self-destructive percolation (van den Berg–Brouwer), where one removes the infinite cluster of a $p_c$-configuration and adds density $\delta$ back, conjecturing that percolation does not recover for small $\delta$.

## 3. History & State of the Art (SOTA)

- **1990.** Bak, Chen and Tang introduce a deterministic forest fire cellular automaton as an SOC candidate.
- **1992.** Drossel and Schwabl add the lightning parameter $\lambda$ and the double separation of time scales $1 \gg \lambda$, $\lambda \gg$ (burning time), giving the model now studied.
- **1993–1994.** Drossel, Clar and Schwabl give the 1D "exact" analysis: $\tau = 2$, $\nu = 1$, with logarithmic corrections; Grassberger and Kantz, Christensen–Flyvbjerg–Olami give early 2D exponent estimates near $\tau \approx 2.1$.
- **2002 — the turning point.** Grassberger (*New J. Phys.* 4, 17) simulates lattices up to $65536^2$ and finds effective exponents that *drift* with $\lambda$ ($\tau_{\text{eff}} \approx 2.10$–$2.15$, $\nu_{\text{eff}} \approx 0.58$, $D_{\text{eff}} \approx 1.96$), concluding that the standard scaling ansatz fails. Pruessner and Jensen (*Phys. Rev. E* 65, 056707, 2002) independently report "broken scaling" and argue the DS model is not critical in the usual sense.
- **2005–2006.** Rigorous era begins: van den Berg and Járai settle the 1D density asymptotics; Dürre constructs and proves uniqueness of the infinite-volume process in $d \ge 2$.
- **2015.** Kiss, Manolescu and Sidoravicius (*Ann. Probab.* 43) prove that planar lattices "do not recover from forest fires" — after a burning event, the configuration stays strictly subcritical at all scales, ruling out the naive self-restoring-criticality picture.

Present status: no critical exponent of the 2D DS model has been rigorously identified, and no proof that any exponent exists.

## 4. Partial Results / Verified Cases

- **$d = 1$, exact asymptotics of the density.** van den Berg and Járai (*Comm. Math. Phys.* 253, 2005) proved that the stationary density of *vacant* sites is of order $\log\log(1/\lambda)/\log(1/\lambda)$, **not** the $1/\log(1/\lambda)$ predicted by Drossel–Clar–Schwabl. The physicists' leading-order prediction is therefore off by a $\log\log$ factor — the first rigorous falsification of an SOC scaling prediction for this model.
- **$d = 1$, cluster structure.** Bressaud and Fournier established scaling limits for one-dimensional forest fire processes: after time/space rescaling by $\log(1/\lambda)$ the process converges to an explicit limit ("one-dimensional general forest fire processes", *Ann. Probab.* / *Mém. SMF*), giving $\xi \asymp \log(1/\lambda)$ and a fully described limit object.
- **$d \ge 2$, existence and uniqueness.** Dürre (*Electron. J. Probab.* 11, 2006; *Electron. Commun. Probab.* 11, 2006): the infinite-volume process with the no-infinite-cluster convention exists and is unique for all $\lambda>0$.
- **$d = 2$, structural non-criticality.** Kiss–Manolescu–Sidoravicius (2015): for the forest fire process on planar lattices, at any time the configuration restricted to a burned region has connection probabilities bounded away from the critical ones — recovery to criticality fails.
- **Mean-field.** Ráth and Tóth (*Electron. J. Probab.* 14, 2009) solve the forest fire dynamics on the Erdős–Rényi graph: the model exhibits genuine self-organized criticality with mean-field exponents ($\tau = 5/2$, cluster size cutoff $n^{2/3}$-type scaling) after the gelation time, described by a modified Smoluchowski equation. Crane, Freeman and Tóth extended this to cluster-growth asymptotics.
- **Frozen percolation surrogates.** Aldous (1999) solved frozen percolation on the binary tree exactly; van den Berg–de Lima–Nolin and van den Berg–Nolin proved that 2D volume-frozen percolation has *exceptional scales*, i.e. no single power law — a rigorous instance of the "broken scaling" phenomenon seen numerically in the DS model.

## 5. Principal Obstacles

- **The dynamics is non-local and non-monotone.** A single lightning strike deletes an unbounded cluster. Standard particle-system tools (Liggett's construction, attractiveness, coupling, duality) do not apply; there is no monotonicity in $\lambda$ or in time.
- **No known stationary-measure formula.** Unlike sandpiles (abelian property, burning test, spanning-tree bijection), the DS model has no algebraic structure. There is no abelian group, no matrix-tree theorem, no exactly solvable transfer operator in $d\ge2$.
- **Near-critical percolation control is too weak.** The heuristic requires knowing the configuration after a fire to within $o(1)$ of critical percolation in a scaling sense. Even with SLE$_6$, conformal invariance and Kesten's near-critical scaling relations available at $p_c$ in 2D, the *conditioned, dynamically produced* configurations are not Bernoulli and one cannot import percolation exponents.
- **Recovery fails.** Kiss–Manolescu–Sidoravicius show the correction is not a perturbation: the post-fire environment is uniformly subcritical at the relevant scales. Hence any derivation of $\nu$ from $4/3$ is invalid, and no replacement mechanism is known.
- **Slow, drifting numerics.** Effective exponents move by $\gtrsim 0.05$ per decade in $\lambda$ up to $\lambda \sim 10^{-8}$, so simulation cannot even decide whether limits exist; it can only exclude the naive percolation values.
- **Hierarchy of scales.** Both the physics (Grassberger's "patch" picture) and the rigorous frozen-percolation analogue (exceptional scales) suggest an infinite hierarchy of length scales $\xi_1 \ll \xi_2 \ll \dots$ with different local behaviour, which is incompatible with a single-exponent ansatz.

## 6. The Gap

Proven: existence/uniqueness of the process ($d\ge2$); exact leading asymptotics in $d=1$ including a $\log\log$ correction that refutes the physics prediction; a mean-field solution on random graphs; the *negative* structural statement that 2D configurations do not recover criticality.

Conjectured but unproven: that in $d=2$ the quantities
$$ \tau := -\lim_{\lambda\to0}\lim_{s\to\infty}\frac{\log P_\lambda(|C(0)|=s)}{\log s}, \qquad \nu := -\lim_{\lambda\to 0}\frac{\log \xi(\lambda)}{\log \lambda} $$
*exist at all*. The precise missing step: a quantitative description of the stationary environment on scale $\xi(\lambda)$ — a statement of the form "the law of $\mu_\lambda$ restricted to a box of side $\xi(\lambda)$, rescaled, converges" — together with an identification of the fixed point of the burn-and-regrow renormalization map. Every existing technique yields either an $O(1)$-scale statement (KMS) or a one-dimensional/mean-field exact solution; nothing bridges to a 2D scaling limit.

## 7. Current Research (as of June 2026)

- **Frozen percolation as a tractable proxy.** The Amsterdam (CWI/van den Berg), Geneva/Cambridge (Manolescu, Kiss) and Paris (Nolin) lines continue to develop volume- and size-frozen percolation on $\mathbb{Z}^2$; the exceptional-scales theorem is the sharpest rigorous evidence that DS exponents do not exist as clean power laws. *(frontier — verify: extensions of exceptional scales to the full forest fire dynamics.)*
- **Mean-field / random-graph SOC.** Budapest (Ráth, Tóth) and collaborators study forest fires on configuration models, preferential attachment and inhomogeneous graphs, where critical exponents *are* provable; the open question is which of these are universal.
- **Multiplicative-coalescent and Smoluchowski approaches.** Coupling forest fires to critical random graph scaling limits (Aldous' multiplicative coalescent) to derive $\tau=5/2$-type behaviour in mean field, and to search for the correct low-dimensional analogue.
- **Numerical renormalization.** Large-scale simulations and machine-learning-assisted estimation of drifting exponents; consensus remains that 2D DS is not simply critical. *(frontier — verify: claims of a converged 2D exponent set.)*
- **Self-destructive percolation.** The van den Berg–Brouwer conjecture ($\delta_c > 0$: adding a small density to a $p_c$-configuration whose infinite cluster is removed does not restore percolation) remains the cleanest single statement whose proof would justify the "no recovery" mechanism in a form usable for exponents. It is proven on some non-planar/high-dimensional and tree-like settings and in the 2D forest fire consequence form by KMS.

## 8. Future Work

- Prove the self-destructive percolation conjecture on $\mathbb{Z}^2$ in the quantitative form $\theta(p_c,\delta) = 0$ for $\delta < \delta_c$, then iterate it as a renormalization step for the DS dynamics.
- Establish *existence* of the correlation length exponent — even a two-sided bound $c\lambda^{-\nu_1} \le \xi(\lambda) \le C\lambda^{-\nu_2}$ with explicit $\nu_1,\nu_2$ would be a first — before attempting identification.
- Determine whether the exceptional-scales phenomenon of volume-frozen percolation transfers verbatim, giving a *proof that no single $\tau$ exists*; this would resolve the problem in the negative.
- Develop forest fires on $\mathbb{Z}^d$ for large $d$ or on the hierarchical lattice, where lace expansion / mean-field methods may give $\tau = 5/2$ and an upper critical dimension (conjecturally $d_c = 6$, matching percolation).
- Extend Bressaud–Fournier's 1D scaling limits to quasi-one-dimensional strips $\mathbb{Z} \times \{1,\dots,k\}$ and track exponent behaviour as $k \to \infty$.

## 9. Key References

- **[Foundational]** P. Bak, K. Chen, C. Tang. *A forest-fire model and some thoughts on turbulence.* Physics Letters A 147 (1990), 297–300.
- **[Foundational]** B. Drossel, F. Schwabl. *Self-organized critical forest-fire model.* Physical Review Letters 69 (1992), 1629–1632.
- **[Foundational]** B. Drossel, S. Clar, F. Schwabl. *Exact results for the one-dimensional self-organized critical forest-fire model.* Physical Review Letters 71 (1993), 3739–3742.
- **[SOTA / Numerics]** P. Grassberger. *Critical behaviour of the Drossel–Schwabl forest fire model.* New Journal of Physics 4 (2002), 17.
- **[SOTA / Numerics]** G. Pruessner, H. J. Jensen. *Broken scaling in the forest-fire model.* Physical Review E 65 (2002), 056707.
- **[Rigorous]** J. van den Berg, A. A. Járai. *On the asymptotic density in a one-dimensional self-organized critical forest-fire model.* Communications in Mathematical Physics 253 (2005), 633–644.
- **[Rigorous]** M. Dürre. *Existence of multi-dimensional infinite volume self-organized critical forest-fire models.* Electronic Journal of Probability 11 (2006), 513–539.
- **[Rigorous]** M. Dürre. *Uniqueness of multi-dimensional infinite volume self-organized critical forest-fire models.* Electronic Communications in Probability 11 (2006), 304–315.
- **[Rigorous / SOTA]** D. Kiss, I. Manolescu, V. Sidoravicius. *Planar lattices do not recover from forest fires.* Annals of Probability 43 (2015), 3216–3238.
- **[Rigorous / Mean field]** B. Ráth, B. Tóth. *Erdős–Rényi random graphs + forest fires = self-organized criticality.* Electronic Journal of Probability 14 (2009), 1290–1327.
- **[Rigorous / 1D]** X. Bressaud, N. Fournier. *Asymptotics of one-dimensional forest fire processes.* Annals of Probability 38 (2010), 1783–1816.
- **[Related]** D. J. Aldous. *The percolation process on a tree where infinite clusters are frozen.* Mathematical Proceedings of the Cambridge Philosophical Society 128 (2000), 465–477.
- **[Related]** J. van den Berg, R. Brouwer. *Self-destructive percolation.* Random Structures & Algorithms 24 (2004), 480–501.
- **[Related]** J. van den Berg, B. N. B. de Lima, P. Nolin. *A percolation process on the square lattice where large finite clusters are frozen.* Random Structures & Algorithms 40 (2012), 220–226.
- **[Survey]** J. van den Berg, P. Nolin. *Forest fires and frozen percolation: a survey of rigorous results* (lecture notes / survey articles on two-dimensional forest fire and frozen percolation processes), 2010s.
- **[Survey]** S. Clar, B. Drossel, F. Schwabl. *Forest fires and other examples of self-organized criticality.* Journal of Physics: Condensed Matter 8 (1996), 6803–6824.

## 10. Worked Example / Concrete Special Case

**Derivation of the scaling relation $\lambda_{\mathrm{cut}}(3-\tau)=1$, and the numerical contradiction.**

Take $d=2$ and assume the standard ansatz: in the stationary state, the number density of clusters of size $s$ is
$$ n_\lambda(s) \;=\; A\, s^{-\tau} \Phi(s/s_{\max}), \qquad s_{\max} = \lambda^{-\lambda_{\mathrm{cut}}}, $$
with $\Phi$ smooth, $\Phi(0)=1$, decaying fast at $\infty$, and $2<\tau<3$.

*Step 1 — the burned mass.* Lightning hits site $x$ at rate $\lambda$; if $x$ lies in a cluster of size $s$, $s$ trees burn. The number of sites in clusters of size $s$ per unit volume is $s\,n_\lambda(s)$, so the burning rate per site is
$$ R_{\mathrm{burn}} \;=\; \lambda \sum_{s\ge1} s\cdot s\, n_\lambda(s) \;=\; \lambda A \sum_s s^{2-\tau}\Phi(s/s_{\max}). $$

*Step 2 — evaluate the sum.* Since $2-\tau > -1$, the sum is dominated by $s \approx s_{\max}$:
$$ \sum_s s^{2-\tau}\Phi(s/s_{\max}) \;\asymp\; s_{\max}^{\,3-\tau}\int_0^\infty u^{2-\tau}\Phi(u)\,du \;=\; c\, s_{\max}^{\,3-\tau}. $$

*Step 3 — balance.* Growth per site is $1-\rho(\lambda)$, which converges to a positive constant $1-\rho_\infty$ (simulations give $\rho_\infty \approx 0.4084$ on $\mathbb{Z}^2$). Setting $R_{\mathrm{grow}} = R_{\mathrm{burn}}$:
$$ 1-\rho_\infty \;=\; cA\,\lambda\, \lambda^{-\lambda_{\mathrm{cut}}(3-\tau)} \quad\Longrightarrow\quad \lambda_{\mathrm{cut}}(3-\tau) = 1. $$

*Step 4 — plug in the two candidate exponent sets.*

| Ansatz | $\tau$ | $\lambda_{\mathrm{cut}} = 1/(3-\tau)$ | $D$ | $\nu = \lambda_{\mathrm{cut}}/D$ |
|---|---|---|---|---|
| Critical percolation values | $187/91 \approx 2.055$ | $1.058$ | $91/48 \approx 1.896$ | $0.558$ |
| Grassberger (2002) measured | $\approx 2.15$ | $\approx 1.18$ | $\approx 1.96$ | $\approx 0.58$ |

The measured $\tau \approx 2.15$ sits about $0.10$ above the percolation value $187/91$ — far outside the numerical error bars — and, crucially, $\tau_{\mathrm{eff}}$ keeps increasing as $\lambda$ decreases through $10^{-4}, 10^{-6}, 10^{-8}$ rather than settling. So the scaling relation of Step 3 is consistent, but the *inputs* are not stable.

*Step 5 — the rigorous cross-check in $d=1$.* The same style of heuristic in one dimension gives vacancy density $1-\rho \asymp 1/\log(1/\lambda)$. van den Berg and Járai proved the truth is $\asymp \log\log(1/\lambda)/\log(1/\lambda)$. The heuristic is therefore wrong already in the only dimension where the answer is known — which is precisely why the 2D exponent values in the table above cannot be trusted, and why the problem is open in the strong form "do the exponents exist?"

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*