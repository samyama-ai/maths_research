---
id: 09-probability/exact-escape-rate-galton-watson-tree
title: "Exact Escape Rate on Galton-Watson Trees"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Exact Escape Rate on Galton-Watson Trees

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/exact-escape-rate-galton-watson-tree` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $T$ be a supercritical Galton–Watson (GW) tree with offspring law $p = (p_k)_{k\ge 0}$, mean $m = \sum_k k p_k > 1$, conditioned on non-extinction. For a bias parameter $\lambda > 0$, the **$\lambda$-biased random walk** $(X_n)_{n \ge 0}$ started at the root $\rho$ moves from a vertex $v \ne \rho$ to its parent with probability $\lambda/(\lambda + d_v)$ and to each of its $d_v$ children with probability $1/(\lambda + d_v)$.

It is a theorem that the **escape rate** (speed)
$$\ell(\lambda, p) \;=\; \lim_{n \to \infty} \frac{|X_n|}{n} \qquad \text{(a.s., } |X_n| = \text{graph distance to } \rho)$$
exists and is a deterministic constant. The open problem is:

> **Compute $\ell(\lambda,p)$ in closed form**, i.e. as an explicit functional of the offspring law $p$ and $\lambda$, for all $\lambda \neq 1$; and, failing that, establish the qualitative structure of $\lambda \mapsto \ell(\lambda,p)$ — in particular the **Lyons–Pemantle–Peres monotonicity conjecture**: for GW trees without leaves ($p_0 = 0$), $\lambda \mapsto \ell(\lambda)$ is strictly decreasing on $[1, m)$.

A complete solution means either an explicit formula (a finite expression in the moments/generating function of $p$ and $\lambda$), or a proof that no such formula exists in a precise sense, together with a proof of monotonicity and regularity of $\ell$.

## 2. Mathematical Foundations

**GW measure.** $\mathbf{GW}$ is the law of $T$; $f(s) = \sum_k p_k s^k$ is the offspring generating function, $q = \mathbf{P}(\text{extinction})$ the smallest root of $f(q) = q$ in $[0,1]$.

**Augmented GW.** $\mathbf{AGW}$ is the law of a tree whose root has $\nu \sim p$ children *plus* one extra parent-edge; it is the natural stationary law for the environment seen from the particle at $\lambda = 1$.

**Electrical formulation.** The $\lambda$-biased walk is reversible with conductances $c(e) = \lambda^{-|v|}$ on the edge $e$ joining $v$ to its parent. Transience holds iff the effective conductance $\mathcal{C}(T)$ from $\rho$ to infinity is positive, and $\mathcal{C}$ satisfies the recursive distributional equation (RDE)
$$\mathcal{C} \;\stackrel{d}{=}\; \frac{1}{\lambda}\sum_{i=1}^{\nu} \frac{\mathcal{C}_i}{1 + \mathcal{C}_i},\qquad \mathcal{C}_i \text{ i.i.d. copies, independent of } \nu \sim p. \tag{2.1}$$
The quenched escape probability from the root is $\beta(T) = \lambda\,\mathcal{C}(T)/\nu(\rho)$.

**Phase diagram** (Lyons 1990; Lyons–Pemantle 1992). Conditioned on survival, the walk is a.s. recurrent for $\lambda \ge m$ and transient for $\lambda < m$: the critical bias is $\lambda_c = m$.

**Existence of the speed** (Lyons–Pemantle–Peres 1995, 1996). $|X_n|/n \to \ell(\lambda,p)$ a.s.; the proof uses the ergodicity of the environment seen from the particle under a **harmonic-stationary measure** $\mathbf{HARM}$, together with a regeneration structure (times $\tau_k$ after which the walk never backtracks below its current level), giving
$$\ell = \frac{\mathbf{E}[|X_{\tau_2}| - |X_{\tau_1}|]}{\mathbf{E}[\tau_2 - \tau_1]} . \tag{2.2}$$
The difficulty is that $\mathbf{HARM}$ (equivalently, the regeneration law) is not explicit for $\lambda \ne 1$.

**The $\lambda = 1$ identity.** For simple random walk, $\mathbf{AGW}$ *is* stationary and reversible for the environment process, and
$$\ell(1,p) \;=\; \mathbf{E}\!\left[\frac{\nu - 1}{\nu + 1}\right], \qquad \nu \sim p. \tag{2.3}$$

## 3. History & State of the Art (SOTA)

- **1990–1992.** R. Lyons determines the recurrence/transience threshold $\lambda_c = m$ for biased walks on trees, via the Nash-Williams/flow criterion and first-passage percolation (Lyons 1990; Lyons–Pemantle, *Ann. Probab.* 1992).
- **1995.** Lyons, Pemantle and Peres prove existence of the speed for SRW and derive the exact formula (2.3), simultaneously computing the dimension of harmonic measure. This is the one case where the escape rate is genuinely closed-form.
- **1996.** The same authors treat general $\lambda$: $\ell(\lambda) > 0$ for $\lambda < m$ on trees without leaves, $\ell = 0$ for $\lambda \ge m$; they pose the monotonicity conjecture and note that no explicit formula is available.
- **2008.** Peres–Zeitouni prove an annealed CLT for $|X_n| - n\ell$ in the ballistic regime, and a $\sqrt{n}$-scale limit at $\lambda = m$.
- **2012.** Ben Arous, Fribergh, Gantert, Hammond analyse trees **with leaves**: dead-end traps of depth $h$ hold the walk for time $\asymp \lambda^{h}$ while trap depths have tail governed by $f'(q) < 1$. The resulting tail index of regeneration times is $\gamma = \log(1/f'(q))/\log\lambda$, giving $\ell(\lambda) = 0$ with $|X_n| \approx n^{\gamma}$ once $\gamma < 1$, and stable (non-Gaussian) fluctuations for $\gamma \in (1,2)$.
- **2014.** Aïdékon expresses $\ell(\lambda)$ through the invariant measure of the environment seen from the particle, built explicitly from the solution of the conductance RDE (2.1) — a formula, but one whose ingredients require solving (2.1).
- **2014.** Ben Arous–Fribergh–Sidoravicius prove the LPP monotonicity conjecture for **large** bias.

## 4. Partial Results / Verified Cases

| Case | Result |
|---|---|
| $\lambda = 1$, any $p$ with $m>1$ | $\ell = \mathbf{E}[(\nu-1)/(\nu+1)]$, exact (LPP 1995) |
| Deterministic $b$-ary tree ($p_b = 1$), $0<\lambda<b$ | $\ell = \dfrac{b-\lambda}{b+\lambda}$, exact |
| $\lambda \ge m$ | $\ell = 0$ (LPP 1996); $|X_n| \asymp \sqrt{n}$ at $\lambda = m$ (Peres–Zeitouni 2008) |
| $p_0 = 0$, $\lambda < m$ | $\ell > 0$; annealed and quenched CLTs (Peres–Zeitouni 2008; Bowditch 2018) |
| $p_0 > 0$, $\lambda > 1/f'(q)$ | $\ell = 0$, $|X_n| = n^{\gamma + o(1)}$, $\gamma = \log(1/f'(q))/\log\lambda < 1$ (BAFGH 2012) |
| $\lambda \to 1$ | Einstein relation: $\ell'(1)$ exists and equals an explicit multiple of the $\lambda=1$ diffusivity (Ben Arous–Hu–Olla–Zeitouni 2013) |
| $\lambda \ge \lambda_0(p)$ large | $\ell$ strictly decreasing (Ben Arous–Fribergh–Sidoravicius 2014) |
| Multi-type GW trees | speed exists, CLT (Dembo–Sun 2012) |

Numerically, $\ell(\lambda)$ is computable to several digits by iterating (2.1) (population dynamics / Monte-Carlo on the RDE) or by direct simulation with regeneration times; no simulated curve has ever contradicted monotonicity for $p_0 = 0$.

## 5. Principal Obstacles

- **No explicit stationary measure for $\lambda \ne 1$.** At $\lambda = 1$ the environment seen from the particle is reversible with respect to $\mathbf{AGW}$ (degree-biasing), which produces (2.3) in one line. For $\lambda \ne 1$ the walk is reversible on a *fixed* tree but the environment process is **not reversible**, and its invariant measure $\mathbf{HARM}$ is mutually absolutely continuous with $\mathbf{AGW}$ with a Radon–Nikodym derivative given only as a limit — never in closed form.
- **The RDE (2.1) is unsolvable.** It is a smoothing-type fixed point with the nonlinear map $x \mapsto x/(1+x)$; outside the deterministic ($b$-ary) case its solution has no known density, no known moments beyond crude bounds, and is not stable under any tractable transform (no Laplace/Mellin closure).
- **Speed is not a local functional.** By (2.2), $\ell$ depends on the whole regeneration excursion law, which couples all scales of the tree; truncation to depth $k$ converges but with no controlled expansion.
- **Trapping destroys perturbative arguments.** With leaves, the regeneration time has a heavy tail with $\lambda$-dependent index, so derivatives in $\lambda$ can fail to exist where $\gamma$ crosses integers; analyticity of $\ell$ is therefore not available as a tool.
- **Monotonicity has no coupling.** Increasing $\lambda$ both pushes the walk toward the root (slower) and shortens backtracking excursions (faster); no monotone coupling of the two $\lambda$-walks on a common tree is known. The BAFS proof works only because at high bias the walk is nearly deterministic along the backbone.

## 6. The Gap

Proved: existence, positivity threshold, $\lambda=1$ formula, $b$-ary formula, asymptotics at $\lambda \uparrow m$ and $\lambda \to \infty$, first-order behaviour at $\lambda = 1$. Unproved: any closed form for $\ell(\lambda,p)$ at a single pair $(\lambda,p)$ with $\lambda \ne 1$ and $p$ non-degenerate; monotonicity on the whole interval $[1,m)$; smoothness/analyticity of $\ell$ in $\lambda$ on $(0,m)$.

The precise barrier is (2.1): one must either **solve the conductance RDE** for a non-degenerate $p$, or find a **second stationarity identity** for $\lambda \ne 1$ that plays the role degree-biasing plays at $\lambda = 1$ — e.g. an explicit cocycle or an entropy identity linking $\ell$, the dimension of harmonic measure, and the Hausdorff dimension $\log m$ of the boundary.

## 7. Current Research (as of June 2026)

- **RDE analysis.** Groups working on recursive distributional equations (Aldous–Bandyopadhyay school; INRIA/Paris and Oxford probability) study regularity and tail behaviour of solutions of (2.1); partial regularity of the law of $\mathcal{C}$ has been claimed for offspring laws with bounded support *(frontier — verify)*.
- **Monotonicity at moderate bias.** Extensions of the Ben Arous–Fribergh–Sidoravicius method (NYU, Montréal) aim to lower $\lambda_0(p)$; the case $\lambda$ near $1$ is being attacked by Einstein-relation perturbation *(frontier — verify)*.
- **Trapping and scaling limits.** Fractional-kinetics and Fontes–Isopi–Newman-type limits for the zero-speed regime on trees with leaves continue to be refined; connections to biased walks on supercritical percolation clusters of $\mathbb{Z}^d$ are the main motivation.
- **Harmonic measure.** Dimension-drop questions ($\dim \mathbf{HARM} < \log m$) and the Curien–Le Gall analysis of harmonic measure on random trees supply the dual viewpoint on the same invariant measure.

## 8. Future Work

- Prove monotonicity for all $\lambda \ge 1$, $p_0 = 0$ — the flagship open case, explicitly posed in *Unsolved problems concerning random walks on trees* (LPP 1997).
- Establish analyticity (or identify the exact regularity) of $\lambda \mapsto \ell(\lambda)$ on $(0,m)$; with leaves, determine whether $\ell \in C^{k}$ exactly where $\gamma > k$.
- Obtain a convergent expansion of $\ell$ in $\lambda - 1$ with computable coefficients, extending the Einstein relation to higher order.
- Prove a rigorous "no closed form" statement, e.g. that $\ell(\lambda,p)$ is not algebraic in $\lambda$ for some fixed non-degenerate $p$.
- Transfer any of the above to biased walks on supercritical percolation clusters, where the same trapping mechanism is conjectured to govern the speed.

## 9. Key References

- **[Foundational]** R. Lyons. *Random walks and percolation on trees.* Annals of Probability 18 (1990), 931–958.
- **[Foundational]** R. Lyons, R. Pemantle. *Random walk in a random environment and first-passage percolation on trees.* Annals of Probability 20 (1992), 125–136.
- **[Foundational]** R. Lyons, R. Pemantle, Y. Peres. *Ergodic theory on Galton–Watson trees: speed of random walk and dimension of harmonic measure.* Ergodic Theory and Dynamical Systems 15 (1995), 593–619.
- **[Foundational]** R. Lyons, R. Pemantle, Y. Peres. *Biased random walks on Galton–Watson trees.* Probability Theory and Related Fields 106 (1996), 249–264.
- **[Survey]** R. Lyons, R. Pemantle, Y. Peres. *Unsolved problems concerning random walks on trees.* In *Classical and Modern Branching Processes*, IMA Vol. Math. Appl. 84, Springer, 1997, 223–237.
- **[Survey / Book]** R. Lyons with Y. Peres. *Probability on Trees and Networks.* Cambridge University Press, 2016.
- **[Survey]** O. Zeitouni. *Random walks in random environment.* Lecture Notes in Mathematics 1837 (École d'Été de Probabilités de Saint-Flour XXXI), Springer, 2004.
- **[SOTA]** E. Aïdékon. *Speed of the biased random walk on a Galton–Watson tree.* Probability Theory and Related Fields 159 (2014), 597–617.
- **[SOTA]** G. Ben Arous, A. Fribergh, N. Gantert, A. Hammond. *Biased random walks on Galton–Watson trees with leaves.* Annals of Probability 40 (2012), 280–338.
- **[SOTA]** G. Ben Arous, A. Fribergh, V. Sidoravicius. *Lyons–Pemantle–Peres monotonicity problem for high biases.* Communications on Pure and Applied Mathematics 67 (2014), 519–530.
- **[SOTA]** Y. Peres, O. Zeitouni. *A central limit theorem for biased random walks on Galton–Watson trees.* Probability Theory and Related Fields 140 (2008), 595–629.
- **[SOTA]** G. Ben Arous, Y. Hu, S. Olla, O. Zeitouni. *Einstein relation for biased random walk on Galton–Watson trees.* Annales de l'IHP Probabilités et Statistiques 49 (2013), 698–721.
- **[Recent]** A. Dembo, N. Sun. *Central limit theorem for biased random walk on multi-type Galton–Watson trees.* Electronic Journal of Probability 17 (2012), paper 75.
- **[Recent]** A. Bowditch. *A quenched central limit theorem for biased random walks on supercritical Galton–Watson trees.* Journal of Applied Probability 55 (2018), 610–626.

## 10. Worked Example / Concrete Special Case

**(a) The solvable case: $b$-ary tree.** Take $p_b = 1$, $b \ge 2$. The RDE (2.1) has a deterministic solution: $\mathcal{C} = (b/\lambda)\,\mathcal{C}/(1+\mathcal{C})$ gives $1 + \mathcal{C} = b/\lambda$, so
$$\mathcal{C} = \frac{b - \lambda}{\lambda},\qquad \beta = \frac{\lambda \mathcal{C}}{b} = \frac{b-\lambda}{b},$$
positive exactly when $\lambda < b = m$, recovering the transience threshold. Every vertex $v \ne \rho$ looks identical, so the environment seen from the particle is a single point and the drift is deterministic:
$$\ell(\lambda) = \frac{b}{b+\lambda} - \frac{\lambda}{b+\lambda} = \frac{b-\lambda}{b+\lambda}.$$
Check at $b = 2$: $\ell(1) = 1/3$, $\ell(2) = 0$, $\ell(1/2)=3/5$. Monotone decreasing, as conjectured.

**(b) The unsolved case: a two-point offspring law.** Take $p_1 = p_3 = 1/2$, so $m = 2$, $p_0 = 0$ (no leaves, no traps), $\lambda_c = 2$.

- At $\lambda = 1$, formula (2.3) gives
$$\ell(1) = \tfrac12\cdot\frac{1-1}{1+1} + \tfrac12\cdot\frac{3-1}{3+1} = 0 + \tfrac12\cdot\tfrac12 = \tfrac14 .$$
  Compare with the $2$-ary tree of the same mean, $\ell = 1/3$: the fluctuation in degrees costs speed, because degree-$1$ vertices are "corridors" the walk must traverse in both directions.
- At $\lambda = 3/2$, everything breaks. The RDE becomes
$$\mathcal{C} \stackrel{d}{=} \frac{2}{3}\Big(\tfrac{\mathcal{C}_1}{1+\mathcal{C}_1}\Big)\ \text{w.p. }\tfrac12,\qquad \mathcal{C} \stackrel{d}{=} \frac{2}{3}\sum_{i=1}^{3}\frac{\mathcal{C}_i}{1+\mathcal{C}_i}\ \text{w.p. }\tfrac12 .$$
  This fixed point has no known solution: $\mathcal{C}$ is supported on $(0,\infty)$ with a fractal-looking density obtainable only numerically, and (2.2) then requires integrating the whole regeneration excursion against it. Theory guarantees $0 < \ell(3/2) < \ell(1) = 1/4$ (positivity from $\lambda < m$, the inequality being exactly what monotonicity would assert and what is *not* proven at this moderate bias); simulation places it near $0.1$. No expression for that number in terms of $p_1, p_3, \lambda$ is known.

This is the problem in miniature: the same walk that is a two-line computation at $\lambda = 1$ and on the regular tree becomes, for one non-degenerate offspring law at one non-unit bias, a quantity nobody can write down.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*