---
id: 09-probability/blanket-time-conjecture-for-random-walks
title: "Winkler Blanket Time Conjecture"
topic: 09-probability
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Winkler Blanket Time Conjecture

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/blanket-time-conjecture-for-random-walks` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $G = (V,E)$ be a finite, connected, undirected graph and let $(X_t)_{t \ge 0}$ be the simple random walk (SRW) on $G$. The **cover time** $t_{\mathrm{cov}}(G)$ is the expected time to visit every vertex, maximized over starting points. For $\delta \in (0,1)$, the **$\delta$-blanket time** is the first time at which every vertex has been visited at least a $\delta$-fraction of its stationary share of visits.

**Winkler–Zuckerman blanket time conjecture (1996).** For every fixed $\delta \in (0,1)$ there is a constant $C(\delta) < \infty$, *independent of the graph*, such that for all finite connected $G$,

$$t_{\mathrm{bl}}(G,\delta) \;\le\; C(\delta)\, t_{\mathrm{cov}}(G).$$

The reverse inequality $t_{\mathrm{bl}}(G,\delta) \ge t_{\mathrm{cov}}(G)$ is immediate, so the conjecture asserts $t_{\mathrm{bl}}(\cdot,\delta) \asymp t_{\mathrm{cov}}(\cdot)$ uniformly over all graphs. A complete resolution requires either such a universal $C(\delta)$ or a graph family $\{G_n\}$ with $t_{\mathrm{bl}}(G_n,\delta)/t_{\mathrm{cov}}(G_n) \to \infty$.

**Status.** Proved by Ding, Lee and Peres (*Annals of Mathematics*, 2012). The refined form — whether $t_{\mathrm{bl}}(G,\delta)/t_{\mathrm{cov}}(G) \to 1$ uniformly as $\delta \to 0$ — remains open.

## 2. Mathematical Foundations

**Local times and blanket time.** Let $N_v(t) = \\#\{s \le t : X_s = v\}$ and let $\pi(v) = \deg(v)/(2|E|)$ be the stationary distribution. Define the random variable

$$\mathcal{B}_\delta \;=\; \inf\Big\{ t \ge 0 \;:\; N_v(t) \ge \delta\, \pi(v)\, t \ \ \text{for all } v \in V \Big\}, \qquad t_{\mathrm{bl}}(G,\delta) \;=\; \max_{v_0 \in V} \mathbb{E}_{v_0}\!\left[\mathcal{B}_\delta\right].$$

Cover time is $t_{\mathrm{cov}}(G) = \max_{v_0} \mathbb{E}_{v_0}[\tau_{\mathrm{cov}}]$, $\tau_{\mathrm{cov}} = \inf\{t : \{X_0,\dots,X_t\} = V\}$. Since $\mathcal{B}_\delta \ge \tau_{\mathrm{cov}}$ pointwise, $t_{\mathrm{bl}} \ge t_{\mathrm{cov}}$.

**Effective resistance metric.** Viewing $G$ as an electrical network with unit conductance per edge, the effective resistance $R_{\mathrm{eff}}(u,v)$ is a metric on $V$. Commute times satisfy the Chandra–Raghavan–Ruzzo–Smolensky identity

$$\mathbb{E}_u[\tau_v] + \mathbb{E}_v[\tau_u] \;=\; 2|E| \cdot R_{\mathrm{eff}}(u,v).$$

**Gaussian free field (GFF).** Fix $v_0 \in V$. The GFF $\{\eta_v\}_{v\in V}$ pinned at $v_0$ is the centered Gaussian field with $\eta_{v_0}=0$ and density proportional to $\exp\big(-\tfrac12 \sum_{\{u,v\}\in E}(\eta_u-\eta_v)^2\big)$. Its intrinsic metric is exactly the resistance metric:

$$\mathbb{E}\big[(\eta_u - \eta_v)^2\big] \;=\; R_{\mathrm{eff}}(u,v).$$

**Majorizing measures (Talagrand, Fernique).** For a centered Gaussian process $\{X_t\}_{t\in T}$ with canonical metric $d$,

$$\mathbb{E}\sup_{t\in T} X_t \;\asymp\; \gamma_2(T,d) \;=\; \inf_{\{\mathcal{A}_n\}} \sup_{t\in T} \sum_{n\ge 0} 2^{n/2}\, \mathrm{diam}\big(A_n(t)\big),$$

the infimum over admissible increasing partition sequences with $|\mathcal{A}_n| \le 2^{2^n}$.

**Main theorem (Ding–Lee–Peres 2012).** There are universal constants such that for every finite connected $G$ with $m = |E|$ edges,

$$t_{\mathrm{cov}}(G) \;\asymp\; m \left( \mathbb{E} \max_{v \in V} \eta_v \right)^{2} \;\asymp\; m\,\gamma_2\big(V, \sqrt{R_{\mathrm{eff}}}\big)^2,$$

and consequently $t_{\mathrm{bl}}(G,\delta) \asymp_\delta t_{\mathrm{cov}}(G)$.

**Isomorphism input.** The generalized second Ray–Knight theorem (Eisenbaum–Kaspi–Marcus–Rosen–Shi, 2000) states that for the continuous-time walk with inverse local time $\tau(t)$ at $v_0$,

$$\Big\{ L_v^{\tau(t)} + \tfrac12 \eta_v^2 \Big\}_{v\in V} \;\overset{d}{=}\; \Big\{ \tfrac12 \big(\eta_v + \sqrt{2t}\,\big)^2 \Big\}_{v \in V},$$

with $\eta$ independent of the walk. This is the bridge from local-time fields to Gaussian processes.

## 3. History & State of the Art (SOTA)

- **1988 — Matthews.** The Matthews bounds relate $t_{\mathrm{cov}}$ to maximal hitting times: $t_{\mathrm{cov}} \le t_{\mathrm{hit}}\, H_n$ with $H_n = \sum_{k\le n} 1/k$, plus a matching lower bound over subsets. These were the only general two-sided estimates for decades, and are loose by up to a $\log n$ factor.
- **1991 — Aldous.** Threshold behavior of cover times; identifies when $\tau_{\mathrm{cov}}/t_{\mathrm{cov}} \to 1$ in probability.
- **1996 — Winkler & Zuckerman**, *Multiple cover time* (Random Structures & Algorithms). Introduce blanket time, prove a polylogarithmic-in-$n$ comparison $t_{\mathrm{bl}} = O(t_{\mathrm{cov}} \cdot \mathrm{polylog}\,n)$, and conjecture the constant-factor bound.
- **2000 — Kahn, Kim, Lovász, Vu** (FOCS). Improve to $t_{\mathrm{bl}}(G,\delta) = O_\delta\big(t_{\mathrm{cov}}(G)\,(\log\log n)^2\big)$, and show the Matthews bound is tight only up to $(\log\log n)^2$. This stood as SOTA for a decade.
- **2004 — Dembo, Peres, Rosen, Zeitouni** (Annals of Math.). Exact leading-order cover time of the 2D torus $\mathbb{Z}_n^2$: $\tau_{\mathrm{cov}}/(n\log n)^2 \to 4/\pi$. Establishes the "cover time = maximum of a log-correlated field" paradigm.
- **2011/2012 — Ding, Lee, Peres.** *Cover times, blanket times, and majorizing measures*, STOC 2011 (Best Paper) and Annals of Mathematics 175 (2012), 1409–1471. Prove the GFF characterization above, resolving the blanket time conjecture and, as a byproduct, giving a deterministic polynomial-time $O(1)$-approximation algorithm for cover time (previously only via simulation).
- **2014–2018.** Sharpening: Ding obtains asymptotic (not just constant-factor) cover-time identities for bounded-degree graphs and trees; Zhai proves exponential concentration of $\tau_{\mathrm{cov}}$ around its mean at scale $\sqrt{m\,t_{\mathrm{cov}}}$.

## 4. Partial Results / Verified Cases

Before 2012, sharp $t_{\mathrm{bl}} \asymp t_{\mathrm{cov}}$ was known for restricted classes; these remain the cases with the strongest quantitative control.

- **Complete graph $K_n$ and expanders.** $t_{\mathrm{cov}} \sim n\log n$; blanket time follows from coupon-collector large deviations with explicit $C(\delta) = 1/(1-\delta+\delta\log\delta)$ (Section 10).
- **Trees.** Winkler–Zuckerman and later Ding gave $t_{\mathrm{bl}}(\delta)/t_{\mathrm{cov}} = 1 + o(1)$ as $\delta\to0$ for bounded-degree trees; on the binary tree of depth $k$ ($n = 2^{k+1}-1$), $t_{\mathrm{cov}} \sim 2 n \log^2 2 \cdot k^2 / \dots$ — more usefully, $\mathbb{E}\max \eta \asymp k$ and $m \asymp n$, giving $t_{\mathrm{cov}} \asymp n k^2 = n \log^2 n$.
- **Cycle $C_n$ and paths.** $t_{\mathrm{cov}}(C_n) = \binom{n}{2}$ exactly; local times are controlled by Ray–Knight, so $C(\delta)$ is explicit.
- **Lattice tori $\mathbb{Z}_n^d$, $d \ge 3$.** Transient-type behavior, $t_{\mathrm{cov}} \sim c_d n^d \log n$; blanket-time comparison from Poissonization of local times.
- **$d = 2$ critical case.** $\mathbb{Z}_n^2$ was the main obstruction class pre-2012 (log-correlated local times, Matthews bound loose by $\log\log$); resolved asymptotically by Dembo–Peres–Rosen–Zeitouni (2004) and by DLP in general.
- **Full generality ($\delta$ fixed, all finite connected $G$).** Proved 2012. The constant is universal in $G$ but the dependence on $\delta$ produced by the DLP argument is not optimized.

## 5. Principal Obstacles

The pre-2012 obstacles explain why the problem was hard and where the residual (asymptotic) version still resists.

- **Matthews' bound loses $\log n$.** It compares cover time to $t_{\mathrm{hit}}\log n$, ignoring the geometry of $V$ under $R_{\mathrm{eff}}$. On graphs where the resistance metric has multi-scale structure (trees, $\mathbb{Z}_n^2$), the true cover time sits strictly between the two Matthews bounds, and no chaining-free argument closes the gap.
- **Local times are not independent, not Gaussian.** Blanket time requires a *uniform lower* bound on the whole local-time field, i.e. control of $\min_v L_v^t$. Union bounds over $n$ vertices cost $\log n$; second-moment methods fail because local times at nearby vertices are strongly positively correlated at exactly the scale that matters.
- **Multi-scale correlation.** On $\mathbb{Z}_n^2$ the field $\{\sqrt{L_v}\}$ is log-correlated. Naive decoupling into independent scales produces a $(\log\log n)^2$ loss — precisely the Kahn–Kim–Lovász–Vu barrier.
- **Suprema of non-Gaussian processes.** Fernique–Talagrand majorizing-measure theory gives two-sided control of $\mathbb{E}\sup$ *only* for Gaussian processes. Transporting a lower bound on $\mathbb{E}\sup$ back to the local-time field requires an exact isomorphism, not an inequality; Dynkin-type isomorphisms alone give one direction.
- **No single dominant scale.** Percolation/entropy heuristics that succeed for i.i.d.-like models break because the cover-time maximum is attained on a fractal set of "late points" with nontrivial multifractal spectrum.

## 6. The Gap

DLP closed the original gap by combining three ingredients that were individually available but never assembled: the EKMRS second Ray–Knight isomorphism (converting $L^{\tau(t)}$ to $\eta^2$ exactly), Talagrand's majorizing-measure theorem (two-sided $\mathbb{E}\max\eta \asymp \gamma_2$), and a Sudakov-type "tree of scales" argument giving a matching lower bound for the *covering* functional.

The remaining gap is quantitative, not qualitative:

$$\text{Proved:}\quad 1 \le \frac{t_{\mathrm{bl}}(G,\delta)}{t_{\mathrm{cov}}(G)} \le C(\delta) \qquad\text{vs.}\qquad \text{Open:}\quad \lim_{\delta \to 0}\ \sup_{G} \frac{t_{\mathrm{bl}}(G,\delta)}{t_{\mathrm{cov}}(G)} \overset{?}{=} 1.$$

Equivalently: is the blanket time *asymptotically equal* to the cover time for small $\delta$, uniformly over graphs? The DLP proof passes through the majorizing-measure equivalence, whose constants are non-explicit (they come from the generic-chaining partition construction), so it cannot produce $1+o_\delta(1)$. Also open: identifying $\lim t_{\mathrm{cov}}/\big(m(\mathbb{E}\max\eta)^2\big)$ — believed to be $1$ for bounded-degree graphs whose GFF maximum is not concentrated, proven by Ding (2014) in that regime.

## 7. Current Research (as of June 2026)

- **Asymptotic blanket times.** Extending Ding's $(1+o(1))$ cover-time identity from bounded-degree graphs and trees to general graphs, which would settle the $\delta \to 0$ refinement for those classes. Groups at Penn, Berkeley, Cambridge and the Weizmann Institute. *(frontier — verify)*
- **Log-correlated fields and thick points.** Abe–Biskup and collaborators characterize the point process of exceptionally late/thick points at multiples of the cover time on $\mathbb{Z}_n^2$; Belius–Kistler give the subleading $\log\log$ correction. This yields blanket-time constants $C(\delta)$ with sharp asymptotics on the 2D torus.
- **Concentration.** Zhai's exponential concentration bound is conjecturally not sharp for graphs with $t_{\mathrm{cov}} \gg m \cdot \mathrm{diam}_{R}$; improving it would give blanket times with high probability, not just in expectation. *(frontier — verify)*
- **Algorithmic side.** Deterministic approximation of $\gamma_2$ by semidefinite programming; whether cover time admits a PTAS (rather than $O(1)$-approximation) is open.
- **Beyond reversibility.** Blanket times for non-reversible chains and for random walks in random environment have no GFF analogue; partial results only via Dirichlet-form comparison. *(frontier — verify)*

## 8. Future Work

1. Prove or refute $\sup_G t_{\mathrm{bl}}(G,\delta)/t_{\mathrm{cov}}(G) \to 1$ as $\delta \to 0$. Peres has emphasized this as the natural remaining question.
2. Obtain explicit, near-optimal $C(\delta)$: current proofs give constants of the form $\exp(\mathrm{poly}(1/\delta))$ or unquantified; the complete-graph example suggests $C(\delta) \approx (1-\delta+\delta\log\delta)^{-1}$ is the truth.
3. Develop a *quantitative* majorizing-measure theorem with computable constants, which would upgrade all cover/blanket estimates from $\asymp$ to $\sim$.
4. Extend the isomorphism route to continuous state spaces (Brownian motion on manifolds), where blanket times for covering by $\varepsilon$-balls are only partly understood.
5. Establish blanket-time analogues for random graphs at criticality, where $R_{\mathrm{eff}}$ has scaling-limit structure (CRT, scaling limits of critical percolation clusters).

## 9. Key References

- **[Foundational]** P. Winkler, D. Zuckerman. *Multiple cover time.* Random Structures & Algorithms, 9(4):403–411, 1996.
- **[Foundational]** P. Matthews. *Covering problems for Brownian motion on spheres.* Annals of Probability, 16(1):189–199, 1988.
- **[Foundational]** D. Aldous. *Threshold limits for cover times.* Journal of Theoretical Probability, 4(1):197–211, 1991.
- **[Foundational]** J. Kahn, J. H. Kim, L. Lovász, V. H. Vu. *The cover time, the blanket time, and the Matthews bound.* Proc. 41st IEEE FOCS, 467–475, 2000.
- **[SOTA]** J. Ding, J. R. Lee, Y. Peres. *Cover times, blanket times, and majorizing measures.* Annals of Mathematics, 175(3):1409–1471, 2012. (Conference version: STOC 2011.)
- **[SOTA]** J. Ding. *Asymptotics of cover times via Gaussian free fields: bounded-degree graphs and general trees.* Annals of Probability, 42(2):464–496, 2014.
- **[SOTA]** A. Zhai. *Exponential concentration of cover times.* Electronic Journal of Probability, 23, paper 32, 2018.
- **[Technical]** N. Eisenbaum, H. Kaspi, M. B. Marcus, J. Rosen, Z. Shi. *A Ray–Knight theorem for symmetric Markov processes.* Annals of Probability, 28(4):1781–1796, 2000.
- **[Technical]** M. Talagrand. *Upper and Lower Bounds for Stochastic Processes.* Springer, 2014.
- **[Related]** A. Dembo, Y. Peres, J. Rosen, O. Zeitouni. *Cover times for Brownian motion and random walks in two dimensions.* Annals of Mathematics, 160(2):433–464, 2004.
- **[Related]** D. Belius, N. Kistler. *The subleading order of two dimensional cover times.* Probability Theory and Related Fields, 167:461–552, 2017.
- **[Survey]** D. A. Levin, Y. Peres. *Markov Chains and Mixing Times*, 2nd ed. American Mathematical Society, 2017.
- **[Survey]** M. B. Marcus, J. Rosen. *Markov Processes, Gaussian Processes, and Local Times.* Cambridge University Press, 2006.

## 10. Worked Example / Concrete Special Case

**The complete graph $K_n$.** Here $\pi(v) = 1/n$ for all $v$, and the walk visits a uniformly random vertex (other than the current one) at each step; ignore the self-avoidance correction, which affects nothing at leading order.

*Cover time.* Coupon collector: $t_{\mathrm{cov}}(K_n) = (n-1)H_{n-1} = n\log n\,(1+o(1))$.

*Blanket time.* Run for $t = c\, n\log n$ steps. For a fixed vertex $v$, $N_v(t) \sim \mathrm{Bin}(t, 1/n) \approx \mathrm{Poisson}(\lambda)$ with $\lambda = c\log n$. The blanket condition at $v$ is $N_v(t) \ge \delta t/n = \delta c \log n = \delta\lambda$. Poisson lower deviations give

$$\mathbb{P}\big[N_v(t) < \delta\lambda\big] \;=\; \exp\!\big(-\lambda\, I(\delta)(1+o(1))\big), \qquad I(\delta) := 1 - \delta + \delta\log\delta \in (0,1].$$

Substituting $\lambda = c\log n$: $\mathbb{P}[N_v(t) < \delta\lambda] = n^{-cI(\delta)(1+o(1))}$.

*Union bound (upper).* If $c I(\delta) > 1$, the expected number of vertices failing the condition is $n \cdot n^{-cI(\delta)} \to 0$, so $\mathcal{B}_\delta \le c\,n\log n$ whp.

*Second moment (lower).* The counts $N_v$ are asymptotically independent across $v$ (negatively associated), so if $cI(\delta) < 1$ then $n^{1-cI(\delta)} \to \infty$ vertices fail, and $\mathcal{B}_\delta > c\,n\log n$ whp.

*Conclusion.* $t_{\mathrm{bl}}(K_n,\delta) = \dfrac{n\log n}{I(\delta)}(1+o(1))$, hence

$$\frac{t_{\mathrm{bl}}(K_n,\delta)}{t_{\mathrm{cov}}(K_n)} \;\longrightarrow\; \frac{1}{1-\delta+\delta\log\delta} \;=:\; C_\star(\delta).$$

Numerically: $C_\star(1/2) = (1/2 - \tfrac12\log 2)^{-1} \approx 6.52$; $C_\star(1/10) \approx 1.30$; $C_\star(\delta) \to 1$ as $\delta \to 0$ and $C_\star(\delta)\to\infty$ as $\delta \to 1$. This is exactly the shape the conjecture predicts: a finite $\delta$-dependent constant, no $n$-dependence, and ratio tending to $1$ for small $\delta$ — the last being the still-open uniform statement of Section 6.

*Consistency with the GFF formula.* On $K_n$, $m \asymp n^2$ and $R_{\mathrm{eff}}(u,v) = 2/n$, so the pinned GFF has $\mathbb{E}(\eta_u-\eta_v)^2 = 2/n$ and $\mathbb{E}\max_v \eta_v \asymp \sqrt{(2/n)\log n}$. Then $m(\mathbb{E}\max\eta)^2 \asymp n^2 \cdot \tfrac{\log n}{n} = n\log n$, matching $t_{\mathrm{cov}}(K_n)$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*