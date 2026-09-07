---
id: 09-probability/random-walk-on-the-giant-component-of-erdos-renyi-graphs
title: "Random Walk on the Giant Component of Erdos-Renyi Graphs"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Random Walk on the Giant Component of Erdős–Rényi Graphs

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/random-walk-on-the-giant-component-of-erdos-renyi-graphs` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $G(n,p)$ be the Erdős–Rényi random graph and $p=\lambda/n$ with $\lambda>1$ fixed, so that whp a unique giant component $\mathcal{C}_1$ of size $(\theta_\lambda+o(1))n$ exists. Run simple random walk (SRW) on $\mathcal{C}_1$. The problem: **determine the full quenched asymptotic behaviour of this walk across the whole sparse regime**, in particular

1. the mixing time from a *typical* start and from the *worst* start, with sharp constants;
2. whether **cutoff** holds, and the cutoff **profile** and **window**;
3. the dependence of the leading constant on $\lambda$ — an explicit formula, monotonicity, and the asymptotics as $\lambda\downarrow1$ and $\lambda\to\infty$;
4. the same questions in the near-critical window $p=(1+\varepsilon)/n$, $\varepsilon=\varepsilon(n)\to0$ with $\varepsilon^3n\to\infty$, and the scaling limit of the walk exactly at criticality $\varepsilon=\Theta(n^{-1/3})$;
5. cover time, blanket time, and hitting-time fluctuations to $(1+o(1))$ precision.

A complete resolution means: quenched statements holding for a.e. realization of $G(n,p)$, with constants identified as explicit functionals of $\lambda$ (or of the associated Galton–Watson tree), and matching upper and lower bounds.

## 2. Mathematical Foundations

**The chain.** Given a connected graph $G=(V,E)$, SRW is the reversible Markov chain with $P(x,y)=\mathbf{1}_{\{xy\in E\}}/\deg(x)$ and stationary measure $\pi(x)=\deg(x)/2|E|$. Mixing:
$$d_x(t)=\|P^t(x,\cdot)-\pi\|_{\mathrm{TV}},\qquad t_{\mathrm{mix}}(\delta)=\max_x\min\{t: d_x(t)\le\delta\}.$$
A sequence $G_n$ exhibits **cutoff** if $t_{\mathrm{mix}}(\delta)/t_{\mathrm{mix}}(1-\delta)\to1$ for every $\delta\in(0,1)$. The **relaxation time** is $t_{\mathrm{rel}}=(1-\lambda_2)^{-1}$ where $\lambda_2$ is the second eigenvalue of $P$; always $t_{\mathrm{rel}}-1\le t_{\mathrm{mix}}(1/4)\le t_{\mathrm{rel}}\log(4/\pi_{\min})$.

**Local structure.** For $p=\lambda/n$, $G(n,p)$ converges locally weakly to the Poisson($\lambda$) Galton–Watson tree $\mathcal{T}_\lambda$; the giant exists iff $\lambda>1$, with
$$\theta_\lambda=1-e^{-\lambda\theta_\lambda},\qquad |\mathcal{C}_1|=(\theta_\lambda+o(1))n .$$
Conditioned to survive, $\mathcal{T}_\lambda$ has offspring bias; SRW on it has a.s. **speed** $\nu_\lambda=\lim_t \mathrm{dist}(X_0,X_t)/t>0$ and **asymptotic (Avez) entropy**
$$\mathfrak{h}_\lambda=\lim_{t\to\infty}-\tfrac1t\log \mathbb{P}(X_t=\cdot\mid \mathcal T)\quad\text{(a.s. limit)},$$
both positive (Lyons–Pemantle–Peres 1995). For the $d$-regular analogue $\nu=(d-2)/d$ and $\mathfrak h=\nu\log(d-1)$.

**Anatomy.** Write $\mathcal{C}_1=\mathrm{Kernel}\;\to\;2\text{-core}\;\to\;\mathcal C_1$: the 2-core $\mathcal{C}_1^{(2)}$ is the maximal subgraph of min degree $2$; contracting its degree-2 paths gives the **kernel** $\mathcal K$, a random multigraph of min degree $3$; $\mathcal C_1$ is $\mathcal C_1^{(2)}$ with independent trees hung off each vertex (Ding–Kim–Lubetzky–Peres 2011). For $p=(1+\varepsilon)/n$, $\varepsilon\to0$:
$$|\mathcal C_1|\approx 2\varepsilon n,\quad |\mathcal C_1^{(2)}|\approx 2\varepsilon^2 n,\quad |\mathcal K|\approx \tfrac43\varepsilon^3 n,$$
so kernel edges number $\approx2\varepsilon^3n$, mean 2-core path length $\approx\varepsilon^{-1}$, and mean attached tree size $\approx\varepsilon^{-1}$.

## 3. History & State of the Art (SOTA)

- Erdős–Rényi (1960) established the phase transition at $p=1/n$.
- The mixing question was raised by Benjamini, Kozma and Wormald and independently addressed by **Fountoulakis and Reed (RSA 2008)**: for fixed $\lambda>1$, $t_{\mathrm{mix}}=\Theta(\log^2 n)$ whp. **Benjamini–Kozma–Wormald (RSA 2014)** gave a structural proof via a decomposition of the giant into an expander core with attached "decorations".
- **Nachmias–Peres (Ann. Probab. 2008)** treated the critical window $p=(1\pm O(n^{-1/3}))/n$: the largest component has diameter $\Theta(n^{1/3})$ and $t_{\mathrm{mix}}=\Theta(n)$.
- **Ding–Lubetzky–Peres (Ann. Probab. 2012)** interpolated: for $p=(1+\varepsilon)/n$ with $\varepsilon^3n\to\infty$, $\varepsilon\to 0$,
  $$t_{\mathrm{mix}}(\mathcal C_1)=\Theta\!\left(\varepsilon^{-3}\log^2(\varepsilon^3 n)\right),$$
  which degenerates correctly to $\Theta(n)$ at $\varepsilon\asymp n^{-1/3}$.
- **Berestycki–Lubetzky–Peres–Sly (Ann. Probab. 2018, "Random walks on the random graph")** proved that the $\Theta(\log^2 n)$ worst case is an artifact of atypical starting points: from a *uniformly chosen* start the walk mixes in $(1+o(1))\mathfrak h_\lambda^{-1}\log n$ steps with **cutoff** and window $\sqrt{\log n}$; the companion result gives cutoff on random $d$-regular graphs at $\frac{d}{d-2}\log_{d-1}n$.
- Cover time: **Cooper–Frieze (RSA 2008)** determined the cover time of the giant to $(1+o(1))$, of order $n\log^2n$ with an explicit $\lambda$-dependent constant; **Barlow–Ding–Nachmias–Peres (CPC 2011)** described its evolution through the critical window.
- Scaling limit: **Croydon (Publ. RIMS 2012)** proved that at criticality the walk, rescaled, converges to Brownian motion on the scaling limit of $\mathcal C_1$ — a random real tree with finitely many extra identifications (Addario-Berry–Broutin–Goldschmidt 2012).

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $\lambda>1$ fixed, worst start | $t_{\mathrm{mix}}=\Theta(\log^2n)$ | Fountoulakis–Reed 2008; BKW 2014 |
| $\lambda>1$ fixed, typical start | cutoff at $\mathfrak h_\lambda^{-1}\log n$, window $\sqrt{\log n}$ | BLPS 2018 |
| Random $d$-regular, $d\ge3$ fixed | cutoff at $\frac{d}{d-2}\log_{d-1}n$, explicit constant | BLPS 2018 |
| Non-backtracking walk, given degrees $\ge3$ | cutoff at $\log n/\mathfrak h$, explicit | Ben-Hamou–Salez 2017 |
| $p=(1+\varepsilon)/n$, $\varepsilon^3n\to\infty$ | $t_{\mathrm{mix}}=\Theta(\varepsilon^{-3}\log^2(\varepsilon^3n))$, $t_{\mathrm{rel}}=\Theta(\varepsilon^{-3})$ | Ding–Lubetzky–Peres 2012 |
| Critical window $\varepsilon=\Theta(n^{-1/3})$ | $t_{\mathrm{mix}}=\Theta(n)$, diameter $\Theta(n^{1/3})$; Brownian scaling limit | Nachmias–Peres 2008; Croydon 2012 |
| $np\to\infty$ (connected regime) | cutoff at $\log_{np} n$, spectral gap $\Theta(1)$ | standard expander arguments; BLPS 2018 |
| Cover time, $\lambda>1$ fixed | $(1+o(1))$-asymptotics, order $n\log^2 n$ | Cooper–Frieze 2008 |

## 5. Principal Obstacles

- **Spectral methods are blocked by a factor of $\log n$.** The giant contains dangling paths of length $\Theta(\log n)$, so $t_{\mathrm{rel}}=\Theta(\log^2 n)$ while typical mixing is $\Theta(\log n)$. Any eigenvalue-based bound is off by a $\log n$ factor and can never see cutoff, which by the product-condition heuristic requires $t_{\mathrm{rel}}=o(t_{\mathrm{mix}})$ — here it fails at the worst-case scale.
- **Unbounded, inhomogeneous degrees.** The Poisson degree distribution has no uniform lower bound $\ge3$, so the tree-comparison and non-backtracking spectral arguments that work for random regular graphs (Ben-Hamou–Salez, Bordenave–Caputo–Salez) do not apply directly; degree-1 and degree-2 vertices create traps and dead ends that break the "walk sees a tree forever" picture.
- **No explicit entropy.** $\mathfrak h_\lambda$ and $\nu_\lambda$ for SRW on the Poisson GW tree are given by an implicit harmonic-measure/stationarity equation on the space of environments seen from the particle; there is no closed form, and even continuity/monotonicity in $\lambda$ is not proven by any current method.
- **Non-uniform local geometry.** Cutoff proofs need the entropy of $X_t$ to concentrate; here the environment around a uniform vertex varies (tree decorations of size $\Theta(\log n)$, 2-core paths of length $\Theta(1)$ mixed with hubs), so quenched concentration must be extracted from a random environment with heavy structural fluctuations.
- **Near-critical regime is multi-scale.** For $\varepsilon\to0$ the walk lives on three nested scales (tree decorations $\varepsilon^{-1}$, 2-core paths $\varepsilon^{-1}$, kernel $\varepsilon^3n$). Sharp constants require simultaneously controlling a diffusive time change, an expander mixing step, and an extreme-value problem for the longest path — no single technique handles all three.

## 6. The Gap

Proven: **order** of the mixing time everywhere in $1<\lambda$, $\varepsilon^3n\to\infty$; **sharp constant + cutoff** only from a typical start at fixed $\lambda$, and only with $\mathfrak h_\lambda$ defined implicitly. Open:

- an explicit formula (or even monotonicity in $\lambda$) for $\mathfrak h_\lambda$ and $\nu_\lambda$, and the asymptotics $\mathfrak h_\lambda$ as $\lambda\downarrow1$ (expected $\asymp$ the near-critical scaling $\varepsilon^3$) and as $\lambda\to\infty$ (expected $\mathfrak h_\lambda=\log\lambda-1+o(1)$);
- **cutoff in the near-critical window**: is $t_{\mathrm{mix}}=(c+o(1))\varepsilon^{-3}\log^2(\varepsilon^3n)$ with an identified $c$, and is there cutoff from a typical start at time $\asymp\varepsilon^{-3}\log(\varepsilon^3 n)$?
- the **cutoff profile** — is the limit shape $\delta\mapsto\bar\Phi(\delta)$ Gaussian, as for random regular graphs conjecturally, or determined by the fluctuation of the entropy?
- worst-case constants: the $\Theta(\log^2n)$ bound has no matching constant; the leading term is governed by the longest dangling path, of length $\log n/\log(1/\lambda e^{-\lambda})$ — the corresponding mixing constant is unproven.

## 7. Current Research (as of June 2026)

- **Entropy of walks on random environments.** Groups at NYU (Peres circle), Cambridge/Vienna (Berestycki), and Paris (Salez, Bordenave, Caputo) continue to develop the "environment seen from the particle" method used in BLPS, aiming to make $\mathfrak h_\lambda$ computable via a fixed-point equation for the harmonic measure on $\mathcal T_\lambda$. *(frontier — verify)*
- **Non-backtracking and Ihara-zeta spectral techniques** extended to unbounded degrees, seeking a second proof of cutoff and quantitative spectral radius bounds for $\mathcal C_1$. *(frontier — verify)*
- **Near-critical cutoff.** Work extending Ding–Lubetzky–Peres by combining the kernel's expander cutoff with a Brownian time change on the decorated paths; the expected answer is a sharp constant with a Gaussian profile at scale $\varepsilon^{-3}\log(\varepsilon^3n)$. *(frontier — verify)*
- **Scaling limits beyond criticality**, via resistance-form convergence (Croydon's framework), to get functional limit theorems for local times and cover times in the whole barely-supercritical window. *(frontier — verify)*
- **Cover-time constants** for the near-critical giant, refining Barlow–Ding–Nachmias–Peres to $(1+o(1))$ precision using Gaussian free field / Ding–Lee–Peres isomorphism methods.

## 8. Future Work

1. Prove monotonicity and analyticity of $\lambda\mapsto\mathfrak h_\lambda$ on $(1,\infty)$; derive $\mathfrak h_\lambda\sim c\,\varepsilon^3$ as $\lambda=1+\varepsilon\downarrow1$, joining the two regimes into a single formula.
2. Establish cutoff (with profile) in the near-critical window; this requires a quenched invariance principle for the walk on a decorated random 3-regular-like kernel.
3. Identify the sharp worst-case constant $\lim t_{\mathrm{mix}}/\log^2 n$ at fixed $\lambda$ via extreme-value theory for dangling path lengths.
4. Transfer the results to configuration models with heavy-tailed degrees where $\mathfrak h$ may be infinite or the walk sub-diffusive; identify the boundary of validity.
5. Prove blanket-time / late-point structure results ($\mathcal C_1$ analogues of Dembo–Peres–Rosen–Zeitouni for the torus).

## 9. Key References

- **[Foundational]** P. Erdős, A. Rényi. *On the evolution of random graphs.* Publ. Math. Inst. Hungar. Acad. Sci. 5 (1960), 17–61.
- **[Foundational]** R. Lyons, R. Pemantle, Y. Peres. *Ergodic theory on Galton–Watson trees: speed of random walk and dimension of harmonic measure.* Ergodic Theory Dynam. Systems 15 (1995), 593–619.
- **[Foundational]** N. Fountoulakis, B. Reed. *The evolution of the mixing rate of a simple random walk on the giant component of a random graph.* Random Structures & Algorithms 33 (2008), 68–86.
- **[Foundational]** I. Benjamini, G. Kozma, N. Wormald. *The mixing time of the giant component of a random graph.* Random Structures & Algorithms 45 (2014), 383–407.
- **[SOTA]** A. Nachmias, Y. Peres. *Critical random graphs: diameter and mixing time.* Annals of Probability 36 (2008), 1267–1286.
- **[SOTA]** J. Ding, J. H. Kim, E. Lubetzky, Y. Peres. *Anatomy of a young giant component in the random graph.* Random Structures & Algorithms 39 (2011), 139–178.
- **[SOTA]** J. Ding, E. Lubetzky, Y. Peres. *Mixing time of near-critical random graphs.* Annals of Probability 40 (2012), 979–1008.
- **[SOTA]** N. Berestycki, E. Lubetzky, Y. Peres, A. Sly. *Random walks on the random graph.* Annals of Probability 46 (2018), 456–490.
- **[SOTA]** A. Ben-Hamou, J. Salez. *Cutoff for nonbacktracking random walks on sparse random graphs.* Annals of Probability 45 (2017), 1752–1770.
- **[SOTA]** C. Bordenave, P. Caputo, J. Salez. *Random walk on sparse random digraphs.* Probability Theory and Related Fields 170 (2018), 933–960.
- **[SOTA]** C. Cooper, A. Frieze. *The cover time of the giant component of a random graph.* Random Structures & Algorithms 32 (2008), 401–439.
- **[SOTA]** M. Barlow, J. Ding, A. Nachmias, Y. Peres. *The evolution of the cover time.* Combinatorics, Probability and Computing 20 (2011), 331–345.
- **[SOTA]** D. Croydon. *Scaling limit for the random walk on the largest connected component of the critical random graph.* Publications of RIMS 48 (2012), 279–338.
- **[SOTA]** L. Addario-Berry, N. Broutin, C. Goldschmidt. *The continuum limit of critical random graphs.* Probability Theory and Related Fields 152 (2012), 367–406.
- **[Survey]** D. A. Levin, Y. Peres. *Markov Chains and Mixing Times*, 2nd ed. American Mathematical Society, 2017.
- **[Survey]** R. van der Hofstad. *Random Graphs and Complex Networks, Vol. 1.* Cambridge University Press, 2017.

## 10. Worked Example / Concrete Special Case

**Near-critical anatomy with $\varepsilon=0.1$, $n=10^7$.** Take $p=(1+\varepsilon)/n=1.1\times10^{-7}$, so $\varepsilon^3n=10^4\to\infty$: barely supercritical.

Component sizes from Section 2:
$$|\mathcal C_1|\approx2\varepsilon n=2\times10^6,\quad |\mathcal C_1^{(2)}|\approx2\varepsilon^2n=2\times10^5,\quad |\mathcal K|\approx\tfrac43\varepsilon^3n\approx1.33\times10^4 .$$
The kernel is essentially 3-regular, so it has $\tfrac32|\mathcal K|\approx2\times10^4=2\varepsilon^3n$ edges. Hence:

- average 2-core path (one kernel edge) has length $\dfrac{2\varepsilon^2n}{2\varepsilon^3n}=\varepsilon^{-1}=10$ vertices;
- average tree hanging off a 2-core vertex has $\dfrac{2\varepsilon n}{2\varepsilon^2 n}=\varepsilon^{-1}=10$ vertices.

**Time to cross one kernel edge.** The walk on a path of length $L=\varepsilon^{-1}$ is diffusive: $\asymp L^2=\varepsilon^{-2}=100$ path steps. Each path step is delayed by an excursion into the attached tree; the expected excursion length is proportional to the tree size $\varepsilon^{-1}=10$. Total per kernel edge:
$$\varepsilon^{-2}\cdot\varepsilon^{-1}=\varepsilon^{-3}=10^3\text{ steps.}$$

**Worst-case start.** The longest 2-core path is not $\varepsilon^{-1}$ but $\asymp\varepsilon^{-1}\log(\varepsilon^3n)=10\cdot\log(10^4)\approx92$, since path lengths are geometric with mean $\varepsilon^{-1}$ and there are $\varepsilon^3n$ of them. Starting at the middle of that path, escaping costs $(\varepsilon^{-1}\log(\varepsilon^3n))^2\cdot\varepsilon^{-1}=\varepsilon^{-3}\log^2(\varepsilon^3n)$ steps $\approx10^3\cdot(9.2)^2\approx8.5\times10^4$. This reproduces the Ding–Lubetzky–Peres theorem
$$t_{\mathrm{mix}}=\Theta\!\left(\varepsilon^{-3}\log^2(\varepsilon^3n)\right),$$
and shows the mechanism: the bottleneck is a **single extremal decorated path**, not a global conductance obstruction — the kernel itself, being a random cubic expander on $1.33\times10^4$ vertices, mixes in only $\Theta(\log(\varepsilon^3n))\approx10$ of its own steps.

**Consistency check at criticality.** Setting $\varepsilon=n^{-1/3}$ gives $\varepsilon^{-3}=n$ and $\log^2(\varepsilon^3n)=\log^2 1=O(1)$, recovering $t_{\mathrm{mix}}=\Theta(n)$ (Nachmias–Peres). The gap in Section 6 is exactly the constant hidden in $\Theta(\cdot)$: the heuristic above predicts a specific numerical prefactor from the extreme-value law of path lengths and the excursion-time distribution, but proving concentration of the escape time around that constant — hence cutoff — is open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*