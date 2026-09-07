---
id: 09-probability/extinction-probability-in-branching-random-walks
title: "Extinction Probability in Branching Random Walks"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Extinction Probability in Branching Random Walks

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/extinction-probability-in-branching-random-walks` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A branching random walk (BRW) is a spatial branching process: each particle produces a random point process of children, displaced relative to the parent. Unlike a Galton–Watson process, whose extinction probability is the minimal fixed point of a single generating function, a BRW can go extinct *spatially* — through absorption at a barrier, or through the loss of particles from a fixed region even while the total population explodes.

The problem, in three linked parts:

1. **Absorbing barrier.** For a BRW on $\mathbb{R}$ with displacement point process $\mathcal{L}$ and a killing rule (kill every particle entering $(-\infty,0)$, or below the line $y = -\rho n$), determine the survival probability $q(\rho)$, its critical drift $\rho_c$, its behaviour *at* $\rho_c$, and its near-critical asymptotics as $\rho \uparrow \rho_c$.
2. **Local versus global survival.** For a BRW on an infinite graph $X$ with reproduction parameter $\lambda$, there are two critical values $\lambda_w \le \lambda_s$: above $\lambda_w$ the total population survives, above $\lambda_s$ the population at a fixed site $x$ returns infinitely often. Decide whether *strong local survival* holds at $\lambda = \lambda_s$ for general (non-quasi-transitive) graphs, and characterize the graphs with $\lambda_w < \lambda_s$.
3. **Quantitative form.** Give the extinction probability as an explicit functional of $\mathcal{L}$ — as the minimal solution of a travelling-wave / smoothing-transform fixed-point equation — with computable error terms.

A complete resolution means: a proof of a.s. extinction or of positive survival in each critical case, with matching upper and lower bounds on $q$ near criticality, valid without extra moment or boundedness hypotheses.

## 2. Mathematical Foundations

Let $\mathbb{T}$ be the genealogical tree with root $\varnothing$. Each $u \in \mathbb{T}$ has a position $V(u) \in \mathbb{R}$; children of $u$ are placed at $V(u) + \{$points of an i.i.d. copy of $\mathcal{L}\}$. Write $|u|$ for the generation of $u$. The **log-Laplace transform** is
$$\psi(\theta) \;=\; \log \mathbb{E}\Big[\sum_{|u|=1} e^{-\theta V(u)}\Big] \in (-\infty,\infty],\qquad \theta \ge 0 .$$

**Many-to-one lemma.** If $\psi(\theta) < \infty$, there is a random walk $(S_n)$ with $\mathbb{E}[g(S_1)] = e^{-\psi(\theta)}\,\mathbb{E}\big[\sum_{|u|=1} e^{-\theta V(u)} g(V(u))\big]$ such that for every measurable $F \ge 0$,
$$\mathbb{E}\Big[\sum_{|u|=n} F\big(V(u_1),\dots,V(u_n)\big)\Big] \;=\; \mathbb{E}\Big[e^{\theta S_n + n\psi(\theta)}\,F(S_1,\dots,S_n)\Big].$$

**Speed (Hammersley–Kingman–Biggins).** With $M_n = \min_{|u|=n} V(u)$, on survival
$$\frac{M_n}{n} \longrightarrow \gamma := -\inf_{\theta>0}\frac{\psi(\theta)}{\theta}\quad \text{a.s.}$$

**Boundary case.** Normalize so that
$$\psi(1) = 0,\qquad \psi'(1) = 0 ,$$
i.e. $\mathbb{E}\big[\sum_u e^{-V(u)}\big] = 1$ and $\mathbb{E}\big[\sum_u V(u)e^{-V(u)}\big] = 0$. Then $\gamma = 0$: the minimum has zero speed, and Hu–Shi (2009) and Addario-Berry–Reed (2009) give $M_n = \tfrac{3}{2}\log n + O(1)$, with $M_n - \tfrac{3}{2}\log n$ converging in law (Aïdékon, 2013).

**Additive martingale** $W_n(\theta) = \sum_{|u|=n} e^{-\theta V(u) - n\psi(\theta)}$; **derivative martingale** $D_n = \sum_{|u|=n} V(u) e^{-V(u)}$ in the boundary case, with $D_n \to D_\infty > 0$ on survival (Biggins–Kyprianou, 2004, 2005).

**Killed BRW.** Let $\mathbb{T}^{\rho}$ be the subtree of particles whose ancestral path stays in $[0,\infty)$ after tilting by drift $\rho$. Survival probability $q(\rho) = \mathbb{P}(|\mathbb{T}^\rho| = \infty)$. The extinction probability $s(x) = 1 - q$ started from a single particle at $x$ solves the **travelling-wave fixed point**
$$s(x) \;=\; \mathbb{E}\Big[\prod_{|u|=1} s\big(x + V(u)\big)\Big],\qquad s(x)=1 \text{ for } x<0,$$
the discrete analogue of the FKPP equation $\tfrac12 u'' + \rho u' + u^2 - u = 0$ for branching Brownian motion (BBM).

**Graph BRW.** On a graph $X$ with continuous-time rates, $\lambda_w = 1/\limsup_n (\sum_x \mu^{(n)}(x,y))^{1/n}$-type quantities give
$$\lambda_w = \big(\limsup_n \|\mu^{(n)}\|^{1/n}\big)^{-1},\qquad \lambda_s = \big(\limsup_n \mu^{(n)}(x,x)^{1/n}\big)^{-1},$$
with $\lambda_w \le \lambda_s$, and $\lambda_w < \lambda_s$ characteristic of nonamenable geometry.

## 3. History & State of the Art (SOTA)

- **1974–1976.** Hammersley, Kingman and Biggins establish the linear speed of $M_n$ by subadditivity — the first structural link between extinction under a moving barrier and the convex conjugate of $\psi$.
- **1978.** Kesten studies BBM with absorption at the origin and drift $-\mu$; at the critical drift $\mu_c = \sqrt{2}$ (binary branching at rate 1) the process dies out almost surely, and he obtains bounds on the extinction time and the number of absorbed particles.
- **1988.** Neveu introduces multiplicative martingales and identifies travelling waves of the FKPP equation with fixed points of the smoothing transform; Chauvin–Rouault connect these to BBM with absorption.
- **2004–2005.** Biggins–Kyprianou solve the boundary case of the smoothing transform, giving the complete description of the fixed points $s$ and hence of admissible extinction functionals.
- **2008–2014.** Bertacchi and Zucca develop the graph theory of $\lambda_w$ vs $\lambda_s$, showing strong local survival can fail at $\lambda_s$ and is not monotone in the graph.
- **2009–2013.** Hu–Shi, Addario-Berry–Reed, Aïdékon settle the $\tfrac32\log n$ correction and the limit law of $M_n$, which controls extinction under near-critical barriers.
- **2010–2013.** Aïdékon; Berestycki–Berestycki–Schweinsberg; Maillard obtain tail asymptotics for the total progeny and the genealogy of critically killed BRW/BBM.

Current SOTA: the critical case for the *linear* barrier is settled in one dimension under mild moment assumptions; the near-critical asymptotic $\log q \asymp -c/\sqrt{\varepsilon}$ is proved; the graph-theoretic classification and the non-linear (curved) barrier problem remain open.

## 4. Partial Results / Verified Cases

- **Supercritical drift, $\rho < \rho_c$:** $q(\rho) > 0$, and $1-q$ is the minimal fixed point of the travelling-wave equation (Biggins, 1976; Biggins–Kyprianou, 2005).
- **Critical drift, $\rho = \rho_c$:** almost sure extinction, for BBM (Kesten, 1978) and for BRW in the boundary case under $\mathbb{E}[W_1 \log_+^2 W_1] < \infty$ (Hu–Shi, 2009; Aïdékon, 2010).
- **Near-critical asymptotics:** for a killed BRW with barrier slope $\varepsilon$ below critical, Gantert–Hu–Shi (2011) prove
 $$\log \mathbb{P}(\text{survival}) \;\sim\; -\frac{\pi\,\kappa}{\sqrt{\varepsilon}}\qquad (\varepsilon \downarrow 0),$$
 with $\kappa$ explicit in terms of $\psi''(1)$ — for BBM with drift $\sqrt{2-2\varepsilon}$ this reads $-\pi/\sqrt{2\varepsilon}\,(1+o(1))$ (Berestycki–Berestycki–Schweinsberg, 2011).
- **Total progeny at criticality:** Aïdékon (2010) shows the number $Z$ of particles absorbed at the critical barrier satisfies $\mathbb{P}(Z > n) \sim c\,n^{-1}(\log n)^{-2}$; Maillard (2013) gives the corresponding BBM statement with the constant.
- **Graphs:** on homogeneous trees $\mathbb{T}_d$ ($d \ge 3$) and on quasi-transitive graphs, local extinction holds at $\lambda_s$ (Bertacchi–Zucca, 2008; Liggett, 1996 for the tree contact process analogue). On $\mathbb{Z}^d$ and all amenable Cayley graphs $\lambda_w = \lambda_s$; on nonamenable graphs $\lambda_w < \lambda_s$.
- **Explicit critical drifts:** binary branching with $N(0,1)$ displacements gives $\rho_c = \sqrt{2\log 2} \approx 1.1774$; Poisson$(m)$ offspring with the same displacement gives $\rho_c = \sqrt{2\log m}$.

## 5. Principal Obstacles

- **No exact solvability.** The fixed-point equation $s(x) = \mathbb{E}\prod_u s(x+V(u))$ is a non-local nonlinear equation; unlike the FKPP PDE it admits no phase-plane analysis, and lattice/arithmetic effects in $\mathcal{L}$ break the smoothness that BBM proofs use.
- **Second-moment failure at criticality.** The natural first-moment estimate $\mathbb{E}[\\#\text{survivors}]$ is $\Theta(1)$ at $\rho_c$ while the second moment diverges; Paley–Zygmund gives nothing. The fix — restricting to paths in a barrier of width $L$ — costs a factor $e^{-\pi^2 n/(2L^2)}$ and only ever yields the right exponent, never the constant.
- **Spine decompositions lose the constant.** The many-to-one lemma is exact for one particle but the change of measure carries no information about the correlation structure of the surviving cloud, so sharp constants require a full genealogical (Brownian-coalescent-point-process) analysis, which is currently available only for BBM and for BRW with strong moment hypotheses.
- **Heavy tails.** When $\mathbb{E}[W_1\log_+^2 W_1] = \infty$ or $\psi(\theta) = \infty$ for all $\theta > 0$, the boundary case has no meaning and the speed can be superlinear; no substitute framework exists.
- **Graph geometry.** $\lambda_s$ is defined by a $\limsup$ of return probabilities, which is not continuous or monotone under graph perturbation (Bertacchi–Zucca, 2014); this rules out approximation arguments from finite or transitive graphs.

## 6. The Gap

Proven: for one-dimensional BRW in the boundary case with two logarithmic moments, extinction at the critical linear barrier and $\log q(\varepsilon) \sim -\pi\kappa\varepsilon^{-1/2}$.

Not proven, and the exact boundary:

1. **Second-order term.** Is $\log q(\varepsilon) = -\pi\kappa\varepsilon^{-1/2} + c\log(1/\varepsilon) + O(1)$? For BBM the $O(1)$ constant is conjectural; for lattice BRW even the logarithmic correction is unknown.
2. **Moment hypotheses.** Removing $\mathbb{E}[W_1\log_+^2W_1]<\infty$ requires a truncation scheme that preserves the $\tfrac32\log n$ barrier — no known truncation does.
3. **Curved barriers.** For a barrier $-a n^{\alpha}$ with $\alpha \in (0,1)$, survival/extinction is governed by an integral test analogous to Kolmogorov's; only $\alpha = 1$ and $\alpha = 1/3$ (Faber–Krahn boundary) are understood.
4. **Criticality on general graphs.** Whether $\lambda_s$-strong-local-survival can hold on some infinite graph is open outside the quasi-transitive class.

## 7. Current Research (as of June 2026)

- **Genealogy at criticality.** The Berestycki–Berestycki–Schweinsberg programme (Oxford, Cambridge, UC San Diego) — the Bolthausen–Sznitman coalescent limit for BBM with absorption — is being pushed to lattice BRW and to multitype systems. *(frontier — verify)*
- **$N$-particle systems.** The $N$-BBM / $N$-BRW selection model of Brunet–Derrida, with rigorous work by Bérard–Gouéré, Maillard, and Schweinsberg, treats extinction as a finite-$N$ metastability question; the $\pi^2/(\log N)^2$ speed correction is the finite-$N$ mirror of the $\pi/\sqrt{2\varepsilon}$ survival exponent.
- **Random environment.** BRW in i.i.d. random environment (Comets–Popov; Mallein–Miłoś) has phase transitions in which the quenched and annealed extinction probabilities differ; sharp near-critical asymptotics are open. *(frontier — verify)*
- **Graph BRW.** Bertacchi–Zucca and collaborators (Milano-Bicocca, Politecnico di Milano) continue the classification of strong local survival on non-quasi-transitive and weighted graphs.
- **Multitype and non-lattice extensions.** Mallein and Mallein–Miłoś extend the $\tfrac32\log n$ and barrier results to time-inhomogeneous and multitype BRW, where the critical barrier becomes concave rather than linear.

## 8. Future Work

- Prove a **universal integral test** $\sum_n a_n / n^{3/2}$-type criterion deciding survival under an arbitrary barrier $b(n)$, extending the Biggins–Kyprianou boundary analysis.
- Identify the **$O(1)$ constant** in $\log q(\varepsilon)$ via the coalescent-point-process description of the surviving population.
- Remove moment hypotheses by developing a **truncation-stable derivative martingale**.
- Settle **critical local survival** on general graphs, likely by finding a graph where $\lambda_s$-survival holds — a construction, not a theorem, is the plausible route.
- Transfer results to **branching Lévy processes** (Bertoin–Mallein), where $\psi$ may have no finite exponential moments.

## 9. Key References

- **[Foundational]** J. F. C. Kingman. *The first birth problem for an age-dependent branching process.* Annals of Probability 3 (1975), 790–801.
- **[Foundational]** J. D. Biggins. *The first- and last-birth problems for a multitype age-dependent branching process.* Advances in Applied Probability 8 (1976), 446–459.
- **[Foundational]** H. Kesten. *Branching Brownian motion with absorption.* Stochastic Processes and their Applications 7 (1978), 9–47.
- **[Foundational]** J. Neveu. *Multiplicative martingales for spatial branching processes.* In *Seminar on Stochastic Processes 1987*, Birkhäuser, 1988.
- **[Structural]** J. D. Biggins, A. E. Kyprianou. *Fixed points of the smoothing transform: the boundary case.* Electronic Journal of Probability 10 (2005), 609–631.
- **[SOTA]** Y. Hu, Z. Shi. *Minimal position and critical martingale convergence in branching random walks, and directed polymers on disordered trees.* Annals of Probability 37 (2009), 742–789.
- **[SOTA]** N. Gantert, Y. Hu, Z. Shi. *Asymptotics for the survival probability in a killed branching random walk.* Annales de l'Institut Henri Poincaré (B) 47 (2011), 111–129.
- **[SOTA]** E. Aïdékon. *Tail asymptotics for the total progeny of the critical killed branching random walk.* Electronic Communications in Probability 15 (2010), 522–533.
- **[SOTA]** J. Berestycki, N. Berestycki, J. Schweinsberg. *Survival of near-critical branching Brownian motion.* Journal of Statistical Physics 143 (2011), 833–854.
- **[SOTA]** J. Berestycki, N. Berestycki, J. Schweinsberg. *The genealogy of branching Brownian motion with absorption.* Annals of Probability 41 (2013), 527–618.
- **[SOTA]** E. Aïdékon. *Convergence in law of the minimum of a branching random walk.* Annals of Probability 41 (2013), 1362–1426.
- **[Graphs]** D. Bertacchi, F. Zucca. *Critical behaviors and critical values of branching random walks on multigraphs.* Journal of Applied Probability 45 (2008), 481–497.
- **[Graphs]** D. Bertacchi, F. Zucca. *Strong local survival of branching random walks is not monotone.* Advances in Applied Probability 46 (2014), 400–421.
- **[Graphs]** T. M. Liggett. *Branching random walks and contact processes on homogeneous trees.* Probability Theory and Related Fields 106 (1996), 495–519.
- **[Survey]** Z. Shi. *Branching Random Walks.* École d'Été de Probabilités de Saint-Flour XLII (2012), Lecture Notes in Mathematics 2151, Springer, 2015.
- **[Survey]** D. Bertacchi, F. Zucca. *Recent results on branching random walks.* In *Statistical Mechanics and Random Walks: Principles, Processes and Applications*, Nova Science Publishers, 2012.

## 10. Worked Example / Concrete Special Case

**Setup.** Binary branching: each particle has exactly $2$ children, each displaced by an independent $N(-\rho, 1)$. Then
$$\psi(\theta) = \log\mathbb{E}\Big[\sum_{|u|=1}e^{-\theta V(u)}\Big] = \log 2 + \rho\theta + \tfrac{\theta^2}{2}.$$
The leftmost particle has speed
$$\gamma = -\inf_{\theta>0}\frac{\psi(\theta)}{\theta} = -\inf_{\theta>0}\Big(\frac{\log 2}{\theta} + \rho + \frac{\theta}{2}\Big).$$
The infimum is at $\theta^\ast = \sqrt{2\log 2}$, giving $\gamma = -\rho + \sqrt{2\log 2}$ for the *rightmost* direction after sign conventions: the cloud spreads to the right at rate $\sqrt{2\log 2} - \rho$.

**Critical drift.** Kill any particle entering $(-\infty,0)$. Survival requires the rightmost speed to be positive:
$$\rho_c = \sqrt{2\log 2} = 1.17741\ldots$$
For $\rho < \rho_c$, $q(\rho) > 0$; for $\rho > \rho_c$ the whole cloud drifts into the barrier and $q = 0$. At $\rho = \rho_c$ the process is in the boundary case ($\psi(\theta^\ast)=0$, $\psi'(\theta^\ast)=0$ after tilting), $M_n \approx \tfrac{3}{2\theta^\ast}\log n \to \infty$ but the *minimum over paths kept above 0* fails: extinction is almost sure.

**Near-critical exponent from a strip.** Take $\rho = \rho_c - \varepsilon'$ where $\varepsilon' > 0$ is small, and confine the tilted spine walk to the strip $[0, L]$. Under the tilt at $\theta^\ast$, the many-to-one lemma gives
$$\mathbb{E}\big[\\#\{|u|=n: 0 \le V(u_k) \le L \ \forall k\}\big] \;=\; \mathbb{E}\big[e^{\theta^\ast S_n + n\psi(\theta^\ast)}\mathbf{1}_{\{S \subset [0,L]\}}\big].$$
Two competing exponential rates appear:

- the excess growth from being $\varepsilon'$ below the critical drift, contributing $e^{+\theta^\ast \varepsilon' n}$ (write $\varepsilon = \theta^\ast\varepsilon'$);
- the cost of the tilted walk (variance $1$) staying in $[0,L]$ for $n$ steps, which by the principal Dirichlet eigenvalue of $\tfrac12\partial_{xx}$ on $(0,L)$ is $e^{-\pi^2 n/(2L^2)}$.

The expected population in the strip is therefore $\approx \exp\{n(\varepsilon - \pi^2/(2L^2))\}$, which explodes iff
$$L \;>\; L_c := \frac{\pi}{\sqrt{2\varepsilon}} .$$
To survive, the initial particle must first push a descendant to height $L_c$ without touching $0$. In the critical (zero-drift) walk, the probability that a single particle's progeny ever reaches height $L$ before absorption decays like $e^{-\theta^\ast L}$ up to polynomial factors. Combining,
$$\log q(\varepsilon) \;\approx\; -\theta^\ast L_c \;=\; -\frac{\pi\,\theta^\ast}{\sqrt{2\varepsilon}},$$
which is exactly the form proved by Gantert–Hu–Shi (2011). For BBM with binary branching at rate $1$ and drift $-\sqrt{2-2\varepsilon}$, $\theta^\ast = \sqrt2$ and the formula collapses to the Berestycki–Berestycki–Schweinsberg result $\log \mathbb{P}(\text{survival}) \sim -\pi/\sqrt{2\varepsilon}$.

**What the example does not give.** The heuristic reproduces the exponent $\varepsilon^{-1/2}$ and the constant $\pi\theta^\ast/\sqrt{2}$, but the polynomial prefactor — the $c\log(1/\varepsilon)$ and $O(1)$ terms of §6 — is invisible to it, because the eigenvalue argument treats the surviving cloud as independent particles. Supplying that correction is precisely the open step.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*