---
id: 09-probability/local-limit-theorem-for-random-walks-in-random-environment
title: "Local Limit Theorem for Random Walks in Random Environment"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Local Limit Theorem for Random Walks in Random Environment

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/local-limit-theorem-for-random-walks-in-random-environment` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A random walk in random environment (RWRE) is a two-layer model: transition probabilities are first sampled at random from a product (or ergodic) law $\mathbb{P}$ on the space of environments, then a walk runs in the frozen sample. Central limit theorems (CLTs) for such walks — statements about $P_\omega(X_n \in \sqrt{n}\,A)$ for macroscopic sets $A$ — are known in many regimes. The **local** limit theorem (LLT) asks for the sharper statement at the scale of a single site:

> **Conjecture (quenched LLT).** Let $(X_n)$ be a RWRE on $\mathbb{Z}^d$ in an i.i.d. uniformly elliptic environment which is transient with velocity $v \neq 0$ and satisfies a quenched CLT with nondegenerate covariance $\Sigma$. Then for $\mathbb{P}$-a.e. $\omega$, uniformly over $x$ in compacts,
> $$ \sup_{x\in\mathbb{Z}^d}\ \Big| n^{d/2}\, P_\omega\big(X_n = x\big) - \mathfrak{a}\, g_\Sigma\!\Big(\tfrac{x-nv}{\sqrt n}\Big) \Big| \;\longrightarrow\; 0 , $$
> where $g_\Sigma$ is the Gaussian density with covariance $\Sigma$ and $\mathfrak{a}$ accounts for periodicity/lattice-span corrections.

A complete solution means either a proof of the display above under stated hypotheses (transience in a direction plus enough ballisticity, or balancedness, or dimension restrictions), or a counterexample: a uniformly elliptic i.i.d. environment obeying a quenched CLT for which $n^{d/2}P_\omega(X_n=x)$ fails to converge for a.e. $\omega$. The companion question — the **annealed** LLT for $P(X_n = x) = \mathbb{E}[P_\omega(X_n=x)]$ — is strictly weaker but also open in general in $d \ge 2$ outside the perturbative and ballistic regimes.

## 2. Mathematical Foundations

**Environment space.** Let $\mathcal{P}_d = \{p \in [0,1]^{2d} : \sum_e p(e) = 1\}$ be transition laws to nearest neighbours, and $\Omega = \mathcal{P}_d^{\mathbb{Z}^d}$ with product measure $\mathbb{P} = \mu^{\otimes \mathbb{Z}^d}$. Write $\omega = (\omega(x,\cdot))_{x\in\mathbb{Z}^d}$. The environment is **uniformly elliptic** if $\mathbb{P}(\omega(0,e) \ge \kappa) = 1$ for some $\kappa>0$ and all $|e|=1$.

**Quenched law.** For fixed $\omega$, $P_\omega^x$ is the law of the Markov chain with
$$ P_\omega^x(X_{n+1} = y \mid X_n = z) = \omega(z, y-z), \qquad X_0 = x .$$
The **annealed** (averaged) law is $P^x(\cdot) = \int_\Omega P_\omega^x(\cdot)\, \mathbb{P}(d\omega)$; it is not Markov.

**Environment seen from the particle.** $\bar\omega_n = \theta_{X_n}\omega$ is a Markov process on $\Omega$ with generator $(Rf)(\omega) = \sum_{|e|=1}\omega(0,e) f(\theta_e\omega)$. If an invariant measure $\mathbb{Q} \ll \mathbb{P}$ exists, then $v = \mathbb{E}_{\mathbb{Q}}[\sum_e e\,\omega(0,e)]$ and ergodic-theorem arguments give the LLN.

**Ballisticity conditions.** Sznitman's $(T)_\gamma$ condition in direction $\ell \in S^{d-1}$: for some $\gamma\in(0,1]$,
$$ \limsup_{L\to\infty} L^{-\gamma} \log P\big( X_{T_U} \cdot \ell < 0 \big) < 0 $$
for slabs $U$ of width $L$. Condition $(T')$ is $(T)_\gamma$ for all $\gamma<1$. These force regeneration times $\tau_1 < \tau_2 < \cdots$ (Sznitman–Zerner) at which the walk reaches a new record in direction $\ell$ and never backtracks; the increments $(X_{\tau_{k+1}} - X_{\tau_k}, \tau_{k+1}-\tau_k)$ are i.i.d. under $P(\cdot \mid \text{regeneration})$.

**Reduction to a renewal LLT.** Ballistic RWRE annealed LLT is essentially a two-dimensional lattice renewal theorem for $\sum_k (X_{\tau_{k+1}}-X_{\tau_k},\,\tau_{k+1}-\tau_k)$, requiring $\mathbb{E}[\tau_2-\tau_1] < \infty$ and $\mathbb{E}[|X_{\tau_2}-X_{\tau_1}|^2]<\infty$ plus a non-lattice/aperiodicity condition. The quenched statement is far harder: no i.i.d. structure survives conditioning on $\omega$.

**Balanced environments.** $\omega$ is balanced if $\omega(x,e) = \omega(x,-e)$ for all $x,e$, $\mathbb{P}$-a.s. Then $X_n$ is a martingale and $L_\omega f(x) = \sum_e \omega(x,e)(f(x+e)-f(x))$ is a nondivergence-form discrete elliptic operator; Alexandrov–Bakelman–Pucci and Krylov–Safonov machinery applies.

**Random conductance model (reversible case).** Conductances $\mu_{xy}>0$ on edges, $\omega(x,y) = \mu_{xy}/\mu_x$, $\mu_x = \sum_y \mu_{xy}$. Here the LLT is equivalent to a **local** heat-kernel statement $p_n^\omega(x,y) \approx n^{-d/2} \mu_y\, g_\Sigma(\cdot)$, obtainable from a parabolic Harnack inequality (PHI).

**Sinai regime ($d=1$).** If $\mathbb{E}\log\rho_0 = 0$ with $\rho_x = \frac{1-\omega(x,1)}{\omega(x,1)}$, then $X_n/(\log n)^2$ converges to Sinai's law and $X_n$ localizes: no Gaussian LLT holds; the correct local statement is concentration on $O(1)$ sites around a valley bottom.

## 3. History & State of the Art (SOTA)

- **1975.** Solomon establishes recurrence/transience and the LLN for $d=1$: transient iff $\mathbb{E}\log\rho_0 \neq 0$, with $v \ne 0$ iff $\mathbb{E}\rho_0 < 1$ or $\mathbb{E}\rho_0^{-1}<1$. Kesten–Kozlov–Spitzer identify the stable-law scaling limits governed by $\kappa>0$ solving $\mathbb{E}[\rho_0^{\kappa}]=1$: diffusive only for $\kappa>2$.
- **1982.** Sinai's localization theorem, showing the $(\log n)^2$ regime — a definitive obstruction to a naive universal LLT.
- **1982.** Lawler proves an invariance principle for balanced environments, opening the nondivergence-form PDE route.
- **1999–2004.** Sznitman–Zerner regeneration structure; Sznitman's $(T')$ ballisticity conditions; Zeitouni's Saint-Flour survey consolidates the field.
- **2004–2009.** Quenched invariance principles for reversible models: Sidoravicius–Sznitman; Berger–Biskup and Mathieu–Piatnitski for supercritical percolation clusters. Barlow–Hambly prove PHI and thence a **quenched LLT** on percolation clusters — the first LLT in a genuinely random $d\ge2$ geometry.
- **2008–2012.** Berger–Zeitouni and Rassoul-Agha–Seppäläinen prove quenched CLTs for ballistic and space–time environments. Guo–Zeitouni prove the quenched invariance principle for i.i.d. balanced environments (elliptic case), extended by Berger–Deuschel to the non-elliptic case.
- **2016.** Berger, Cohen and Rosenthal prove an annealed LLT and equivalence of static/dynamic viewpoints for ballistic i.i.d. RWRE under polynomial ballisticity in $d\ge 2$ — the strongest general LLT result to date.
- **2012–2019.** Dolgopyat–Goldsheid obtain sharp quenched and annealed local results in $d=1$ and on strips, including quenched LLTs in the diffusive $\kappa>2$ regime and subdiffusive strip regimes.

## 4. Partial Results / Verified Cases

| Setting | Result | Reference |
|---|---|---|
| $d=1$, nearest-neighbour, $\mathbb{E}\log\rho_0 \ne 0$, $\kappa > 2$ | Quenched and annealed LLTs with explicit random centering | Dolgopyat–Goldsheid (2012) |
| $d=1$ strip, subdiffusive $\kappa \in (0,2)$ | Limit theorems with stable scaling; local statements | Dolgopyat–Goldsheid (2013) |
| $d \ge 2$, i.i.d. uniformly elliptic, polynomial ballisticity $(P)_M$ | **Annealed** LLT $n^{d/2}P(X_n=x) \to \mathfrak{a}\,g_\Sigma$; static $\equiv$ dynamic points of view | Berger–Cohen–Rosenthal (2016) |
| Supercritical bond percolation cluster, $d\ge2$ | Quenched LLT via PHI, Gaussian heat-kernel bounds | Barlow (2004); Barlow–Hambly (2009) |
| Random conductances, uniformly elliptic or with moment conditions $p^{-1}+q^{-1}<2/d$ | Quenched CLT plus local heat-kernel/Harnack estimates | Andres–Deuschel–Slowik (2016) |
| Balanced i.i.d. environments, $d\ge2$ | Quenched invariance principle (elliptic and non-elliptic); LLT-type heat kernel bounds via Krylov–Safonov | Guo–Zeitouni (2012); Berger–Deuschel (2014) |
| Space–time (dynamic, i.i.d. in time) environments | Quenched a.s. invariance principle; LLT reachable by martingale + regeneration | Rassoul-Agha–Seppäläinen (2005) |
| Small perturbations of simple random walk, $d\ge3$ | CLT and heat-kernel control by perturbative expansion | Bricmont–Kupiainen (1991); Sznitman–Zeitouni (2006) |

## 5. Principal Obstacles

- **No spectral gap in a fixed space.** Classical LLTs come from Fourier inversion: $P(X_n=x) = (2\pi)^{-d}\int_{[-\pi,\pi]^d} e^{-i\theta x}\hat\varphi(\theta)^n d\theta$ with $\hat\varphi$ a fixed characteristic function. For RWRE the increments are neither independent nor stationary under $P_\omega$, so no $\hat\varphi^n$ exists; the transfer operator $R$ acts on $L^2(\Omega,\mathbb{Q})$ and typically has **no spectral gap** (its spectrum touches 1 continuously), so perturbation theory in the Nagaev–Guivarc'h style fails.
- **Regeneration is annealed only.** Regeneration times are i.i.d. under $P$, not under $P_\omega$. Conditioning on $\omega$ destroys independence and reintroduces long-range correlation through the environment, which is exactly why Berger–Cohen–Rosenthal reach the annealed and not the quenched LLT.
- **Traps and heavy tails.** In $d=1$ and near-critical $d\ge2$ regimes, $\mathbb{E}[\tau_2-\tau_1]=\infty$ when $\kappa \le 1$; regeneration renewal theory then converges to stable rather than Gaussian laws, and the local density can be non-continuous or the walk can localize (Sinai).
- **Non-reversibility.** The reversible tools that yield LLTs on percolation clusters — Nash–Moser iteration, PHI, Poincaré inequalities on the cluster — have no non-reversible analogue with sharp constants. Nondivergence-form estimates (ABP, Krylov–Safonov) survive only in the balanced case.
- **Error scale.** The LLT demands an error $o(n^{-d/2})$ on a single-site probability, whereas quenched CLTs control only $O(1)$-scale sets; a $n^{-d/2}$-precision statement is not implied by any Berry–Esseen bound currently available for RWRE, where quenched CLT rates are typically only logarithmic.
- **Ballisticity conjecture unresolved.** Whether $0 < \liminf |X_n|/n$ follows from directional transience in $d\ge2$ is itself open, so the hypothesis set for the LLT cannot yet be reduced to transience.

## 6. The Gap

Section 4 gives: (a) full quenched LLTs in $d=1$ under $\kappa>2$; (b) an *annealed* LLT in $d\ge2$ under polynomial ballisticity; (c) *quenched* LLTs only for reversible or balanced (martingale) environments. Section 1 asks for the quenched LLT for general non-reversible, non-balanced ballistic RWRE in $d\ge2$.

The exact missing step: upgrading an annealed local estimate to an $\omega$-a.s. one. Concretely, one needs a concentration bound
$$ \mathbb{P}\Big( \big| n^{d/2}P_\omega(X_n = x) - \mathbb{E}\big[n^{d/2}P_\omega(X_n=x)\big] \big| > \varepsilon \Big) \le C n^{-(1+\delta)} $$
summable in $n$ for Borel–Cantelli. Current variance estimates for $P_\omega(X_n=x)$ in the ballistic non-reversible setting are not $o(1)$ at the local scale, because the environment along the traversed path is used $\Theta(n)$ times and decorrelation of the environment chain is not known to be fast enough. Equivalently: the quenched LLT is the statement that the environment chain mixes in a strong (local, uniform) sense — which is exactly what the absence of a spectral gap denies.

## 7. Current Research (as of June 2026)

- **Extending Berger–Cohen–Rosenthal to the quenched setting.** Groups at Technion (Berger) and Weizmann/NYU (Zeitouni and collaborators) continue to push regeneration + concentration hybrids; the target is a quenched LLT under $(T')$ in $d\ge4$, where two-point function estimates are more tractable. *(frontier — verify)*
- **Renormalization for non-perturbative environments.** Continuation of the Bricmont–Kupiainen and Sznitman–Zeitouni programme with modern multiscale/coarse-graining arguments; recent work aims to remove the smallness of the perturbation in $d\ge3$. *(frontier — verify)*
- **Balanced and non-elliptic environments.** Deuschel, Guo, Ramírez and coauthors work on quenched heat kernel and Harnack estimates in degenerate balanced environments; these are the closest existing route to a bona fide quenched LLT in $d\ge2$.
- **Degenerate random conductances.** Andres, Deuschel, Slowik, Chiarini and collaborators on quenched local CLTs under sharp moment conditions and for time-dependent conductances, including the long-range/heavy-tailed case.
- **One-dimensional refinements.** Dolgopyat, Goldsheid, Peterson, Enriquez–Sabot–Zindy: exact quenched local asymptotics, second-order corrections, and joint scaling limits in the subdiffusive regimes.
- **Stochastic homogenization interface.** Armstrong–Kuusi–Mourrat-type quantitative homogenization gives $O(n^{-\alpha})$ rates for divergence-form models; transferring this to non-divergence, non-reversible RWRE is an active goal.

## 8. Future Work

- Prove a quantitative quenched CLT with polynomial rate for ballistic RWRE; the LLT is then plausibly reachable by a smoothing (Esseen-type) argument on the mesoscopic scale.
- Establish variance decay $\mathrm{Var}_\mathbb{P}\big(n^{d/2}P_\omega(X_n=x)\big) = O(n^{-\delta})$ for some $\delta>0$ under $(T')$ — identified by several authors as the crux.
- Develop a non-reversible parabolic Harnack inequality, or prove it cannot hold uniformly, which would decide whether the reversible route generalizes.
- Settle the ballisticity conjecture in $d\ge2$ (transience in a direction $\Rightarrow$ ballistic), removing the artificial ballisticity hypotheses.
- Produce a counterexample: an environment with a quenched CLT but oscillating $n^{d/2}P_\omega(X_n=x)$, which would show LLT is strictly stronger than CLT for RWRE.
- Complete the $d=1$ picture for $\kappa \le 2$ with quenched local statements at stable scaling, including the marginal case $\kappa=2$.

## 9. Key References

- **[Foundational]** F. Solomon. *Random walks in a random environment.* Annals of Probability 3(1):1–31, 1975.
- **[Foundational]** H. Kesten, M. V. Kozlov, F. Spitzer. *A limit law for random walk in a random environment.* Compositio Mathematica 30(2):145–168, 1975.
- **[Foundational]** Ya. G. Sinai. *The limiting behavior of a one-dimensional random walk in a random medium.* Theory of Probability and Its Applications 27(2):256–268, 1982.
- **[Foundational]** G. F. Lawler. *Weak convergence of a random walk in a random environment.* Communications in Mathematical Physics 87(1):81–87, 1982.
- **[Foundational]** A.-S. Sznitman, M. Zerner. *A law of large numbers for random walks in random environment.* Annals of Probability 27(4):1851–1869, 1999.
- **[SOTA / Recent]** N. Berger, M. Cohen, R. Rosenthal. *Local limit theorem and equivalence of dynamic and static points of view for certain ballistic random walks in i.i.d. environments.* Annals of Probability 44(4):2889–2979, 2016.
- **[SOTA / Recent]** D. Dolgopyat, I. Goldsheid. *Quenched limit theorems for nearest neighbour random walks in 1D random environment.* Communications in Mathematical Physics 315(1):241–277, 2012.
- **[SOTA / Recent]** D. Dolgopyat, I. Goldsheid. *Limit theorems for random walks on a strip in subdiffusive regimes.* Nonlinearity 26(6):1743–1782, 2013.
- **[SOTA / Recent]** X. Guo, O. Zeitouni. *Quenched invariance principle for random walks in balanced random environment.* Probability Theory and Related Fields 152(1–2):207–230, 2012.
- **[SOTA / Recent]** N. Berger, J.-D. Deuschel. *A quenched invariance principle for non-elliptic random walk in i.i.d. balanced random environment.* Probability Theory and Related Fields 158(1–2):91–126, 2014.
- **[SOTA / Recent]** M. T. Barlow, B. M. Hambly. *Parabolic Harnack inequality and local limit theorem for percolation clusters.* Electronic Journal of Probability 14:1–27, 2009.
- **[SOTA / Recent]** S. Andres, J.-D. Deuschel, M. Slowik. *Harnack inequalities on weighted graphs and some applications to the random conductance model.* Probability Theory and Related Fields 164(3–4):931–977, 2016.
- **[SOTA / Recent]** F. Rassoul-Agha, T. Seppäläinen. *An almost sure invariance principle for random walks in a space-time random environment.* Probability Theory and Related Fields 133(3):299–314, 2005.
- **[SOTA / Recent]** N. Berger, O. Zeitouni. *A quenched invariance principle for certain ballistic random walks in i.i.d. environments.* In *In and Out of Equilibrium 2*, Progress in Probability 60, Birkhäuser, 2008, pp. 137–160.
- **[SOTA / Recent]** N. Enriquez, C. Sabot, O. Zindy. *Limit laws for transient random walks in random environment on $\mathbb{Z}$.* Annales de l'Institut Fourier 59(6):2469–2508, 2009.
- **[Survey]** O. Zeitouni. *Random walks in random environment.* Lectures on Probability Theory and Statistics, École d'Été de Saint-Flour XXXI, Lecture Notes in Mathematics 1837, Springer, 2004, pp. 189–312.
- **[Survey]** A.-S. Sznitman. *Topics in random walks in random environment.* ICTP Lecture Notes Series 17, School and Conference on Probability Theory, 2004, pp. 203–266.
- **[Survey]** M. T. Barlow. *Random Walks and Heat Kernels on Graphs.* London Mathematical Society Lecture Note Series 438, Cambridge University Press, 2017.

## 10. Worked Example / Concrete Special Case

**Setting.** $d=1$, nearest-neighbour, i.i.d. environment with two values: $\omega(x,1) = \tfrac{3}{4}$ with probability $\tfrac12$, and $\omega(x,1) = \tfrac12$ with probability $\tfrac12$. So $\rho_x = (1-\omega(x,1))/\omega(x,1) \in \{1/3, 1\}$ with equal probability.

**Step 1 — transience and speed.** $\mathbb{E}\log\rho_0 = \tfrac12\log\tfrac13 + \tfrac12\log 1 = -\tfrac12\log 3 < 0$, so $X_n \to +\infty$ a.s. Solomon's formula gives
$$ \mathbb{E}\rho_0 = \tfrac12\cdot\tfrac13 + \tfrac12 = \tfrac23 < 1, \qquad v = \frac{1-\mathbb{E}\rho_0}{1+\mathbb{E}\rho_0} = \frac{1/3}{5/3} = \frac{1}{5}. $$
The walk is ballistic with speed $v=1/5$.

**Step 2 — tail exponent.** The exponent $\kappa$ solves $\mathbb{E}[\rho_0^{\kappa}] = 1$, i.e. $\tfrac12 3^{-\kappa} + \tfrac12 = 1$, i.e. $3^{-\kappa} = 1$, giving $\kappa = \infty$. All moments of the regeneration time are finite; we are deep in the diffusive regime $\kappa > 2$. A CLT holds: $(X_n - nv)/\sqrt{n} \Rightarrow N(0,\sigma^2)$ with $\sigma^2>0$ computable from regeneration increments.

**Step 3 — what the LLT asserts here.** Because the walk is on $\mathbb{Z}$ with $\pm1$ steps, $X_n$ has parity: $X_n \equiv n \pmod 2$. So the lattice span is $2$ and the correct normalization carries $\mathfrak{a}=2$:
$$ \sqrt{n}\; P_\omega(X_n = x) \;\longrightarrow\; \frac{2}{\sqrt{2\pi\sigma^2}} \exp\!\Big(-\frac{(x - nv - \Delta_n(\omega))^2}{2\sigma^2}\Big), \qquad x \equiv n \ (2). $$
Here $\Delta_n(\omega)$ is an environment-dependent random centering of order $\sqrt{n}$: this is the key discovery of Dolgopyat–Goldsheid. The quenched centering is **not** $nv$; a random shift built from partial sums of $\log\rho$ over the traversed region must be subtracted. Setting $\Delta_n \equiv 0$ makes the statement false, while averaging over $\omega$ restores the plain annealed form $\sqrt{n}\,P(X_n=x) \to 2\,g_{\tilde\sigma^2}(x/\sqrt n - \sqrt n v)$ with a strictly larger annealed variance $\tilde\sigma^2 > \sigma^2$.

**Step 4 — the moral.** Even in this fully solvable binary example, the quenched local density differs from the annealed one by a $\sqrt{n}$-scale random translation, and the two variances differ. In $d\ge2$ the analogue of $\Delta_n(\omega)$ is not identified, and no summable concentration bound is known for it — which is precisely the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*